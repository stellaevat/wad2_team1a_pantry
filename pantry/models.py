import os
from django.utils.deconstruct import deconstructible
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import inflect

p = inflect.engine()

# Sets name of media when saved, to make sense for relevant model
@deconstructible
class FileRenamed(object):
    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        if isinstance(instance, Recipe):
            filename = f"{instance.slug}.{ext}"
        elif isinstance(instance, UserProfile):
            filename = f"{instance.user.username}.{ext}"
        else:
            filename = f"{instance.pk}.{ext}"
        return os.path.join(self.path, filename)


class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)
    slug = models.SlugField(unique=True)
    # Whether the category will be used as a tab
    tab = models.BooleanField(default=False)
    # Whether users adding recipes will be able to select this category as a tag
    # Alternatively will be added automatically based on recipe info (e.g. time/difficulty)
    selectable = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Ingredient(models.Model):
    TYPES = (("meats", "Meat, Seafood & Substitutes"),
            ("dairy", "Eggs, Dairy & Substitutes"),
            ("veg", "Vegetables & Funghi"),
            ("pulses", "Pulses"),
            ("grains", "Grains, Seeds & Nuts"),
            ("carbs", "Bread, Pasta & Rice"),
            ("fats", "Fats & Oils"),
            ("herbs", "Herbs, Spices & Seasonings"),
            ("condiments", "Condiments & Sauces"),
            ("fruit", "Fruit"),
            ("baking", "Sweet & Baking"),
            ("drinks", "Beverages"))
            
    name = models.CharField(max_length=20,unique=True)
    ingredient_type = models.CharField(max_length=16, choices=TYPES)
    

    def __str__(self):
        return self.name

    def get_plural(self):
        if self.name[-1] == "y":
            return self.name[:-1] + "ies"
        return p.plural(self.name)
        
    @classmethod
    def get_types(cls):
        return cls.TYPES

class Recipe(models.Model):
    DIFFICULTIES = (("easy", "Easy"),
                    ("medium", "Medium"),
                    ("advanced", "Advanced")) 
                    
    title = models.CharField(max_length=128, unique=True)
    picture = models.ImageField(upload_to=FileRenamed('recipe_pictures'), blank=True, default='recipe_pictures/banner-default.png')
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    servings = models.IntegerField()
    difficulty = models.CharField(max_length = 16, choices = DIFFICULTIES)
    steps = models.CharField(max_length=2048)
    category = models.ManyToManyField(Category)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientList')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        
    @classmethod
    def get_difficulties(cls):
        return cls.DIFFICULTIES
        
class IngredientList(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=16)
    plural = models.BooleanField(default=False)
    
    class Meta:
        unique_together = [['recipe', 'ingredient']]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Recorded in UserProfile to make it a unique field
    email = models.EmailField(max_length=254, unique=True)
    profile_picture = models.ImageField(upload_to=FileRenamed('profile_pictures'), blank=True, default='profile-picture-default.png')
    starred = models.ManyToManyField(Recipe, related_name="users")

    def __str__(self):
        return self.user.username
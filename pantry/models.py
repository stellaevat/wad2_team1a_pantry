from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(unique=True)
    # Whether the category will be used as a tab
    tab = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Ingredient(models.Model):
    types = (("meats", "Meat, Seafood & Substitutes"),
            ("dairy", "Eggs, Dairy & Substitutes"),
            ("veg", "Vegetables & Funghi"),
            ("pulses", "Pulses"),
            ("grains", "Grains, Seeds & Nuts"),
            ("carbs", "Bread, Pasta & Rice"),
            ("fats", "Fats & Oils"),
            ("herbs", "Herbs & Spices"),
            ("condiments", "Condiments & Sauces"),
            ("fruit", "Fruit"),
            ("sweets", "Sweet & Baking"),
            ("drinks", "Beverages"))
            
    name = models.CharField(max_length=128,unique=True)
    ingredient_type = models.CharField(max_length = 128, choices=types)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_types(cls):
        return cls.types
        

class Recipe(models.Model):
    title = models.CharField(max_length=128,unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    steps = models.CharField(max_length=2048)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientList')
    prep_time = models.IntegerField()
    category = models.ManyToManyField(Category)
    cook_time = models.IntegerField()
    servings = models.IntegerField()
    difficulty = models.CharField(
        max_length = 16,
        choices = (
            ("easy", "Easy"),
            ("medium", "Medium"),
            ("advanced", "Advanced")
        ) 
    )
    picture = models.ImageField(upload_to='recipe_pictures', blank=True)
    pub_date = models.DateField()
    stars = models.IntegerField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        
class IngredientList(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=16)
    
    class Meta:
        unique_together = [['recipe', 'ingredient']]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    starred = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.user.username
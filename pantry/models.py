from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Ingredient(models.Model):
    name = models.CharField(max_length=128,unique=True)
    ingredient_type = models.CharField(
        max_length = 128,
        choices=(
            ("meats", "Meat, Seafood & Substitutes"),
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
            ("drinks", "Beverages")
        )
    )

    def __str__(self):
        return self.name

class SiteUser(models.Model):
    email = models.CharField(max_length=254, unique = True)
    username = models.CharField(max_length=128,unique = True)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    title = models.CharField(max_length=128,unique = True)
    author = models.ForeignKey(SiteUser, on_delete=models.CASCADE, null=True)
    steps = models.CharField(max_length=2048)
    ingredients = models.ManyToManyField(Ingredient)
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


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    Title = models.CharField(max_length=128)
    Steps = models.CharField(max_length=2048)
    PrepTime = models.IntegerField()
    CookTime = models.IntegerField()
    Servings = models.IntegerField()
    Difficulty = models.CharField(
        max_length = 16,
        choices = (
            ("easy", "Easy"),
            ("medium", "Medium"),
            ("hard", "Hard")
        ) 
    )
    Picture = models.ImageField(upload_to='recipe_pictures', blank=True)
    PubDate = models.DateField()
    Start = models.IntegerField()

    def __str__(self):
        return self.Title

class User(models.Model):
    Email = models.CharField(max_length=254)
    Username = models.CharField(max_length=128)
    Password = models.CharField(max_length=128)
    ProfilePicture = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.Username

class Category(models.Model):
    Name = models.CharField(max_length=128)

    def __str__(self):
        return self.Name

class Ingredient(models.Model):
    Name = models.CharField(max_length=128)
    Type = models.CharField(
        max_length = 128,
        choices=(
            ("meat", "Meat, seafood & substitutes"),
            ("eggs", "Eggs, dairy & substitutes"),
            ("veg", "Vegetables & Funghi"),
            ("pulses", "Pulses"),
            ("grains", "Grains, seeds & nuts"),
            ("bread", "Bread, pasta & rice"),
            ("fats", "Fats & Oils"),
            ("herbs", "Herbs & Spices"),
            ("condiments", "Condiments & Sauces"),
            ("fruit", "Fruit"),
            ("sweets", "Sweet & Baking"),
            ("beverages", "Beverages")
        )
    )

    def __str__(self):
        return self.Name

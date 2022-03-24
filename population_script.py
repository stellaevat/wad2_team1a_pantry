import os
from django import urls
from datetime import datetime
from ingredient_population import get_all_ingredients
from recipe_population import get_all_recipes
import pytz

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wad2_team1a_pantry.settings")

import django
django.setup()
from pantry.models import Category, Recipe, UserProfile, Ingredient, IngredientList
from django.contrib.auth.models import User

def populate():

    users = [
        {"email" : "johndoe@gmail.com", "username" : "johndoe", "password" : "password", "filename" : "johndoe.jpg"},
        {"email" : "benking@gmail.com", "username" : "benking", "password" : "password", "filename" : "benking.jpg"},
        {"email" : "joebloggs@gmail.com", "username" : "joebloggs", "password" : "password", "filename" : "joebloggs.jpg"},
        {"email" : "sallywalker@gmail.com", "username" : "sallywalker", "password" : "password", "filename" : "sallywalker.jpg"}
    ]

    categories = [
        {"name" : "Mains", "tab" : True, "selectable" : True},
        {"name" : "Appetizers", "tab" : True, "selectable" : True},
        {"name" : "Desserts", "tab" : True, "selectable" : True},
        {"name" : "Easy Meals", "tab" : True, "selectable" : False},
        {"name" : "Under 30'", "tab" : True, "selectable" : False},
        {"name" : "Healthy", "tab" : False, "selectable" : True},
        {"name" : "Vegan", "tab" : False, "selectable" : True},
        {"name" : "Vegetarian", "tab" : False, "selectable" : True},
        {"name" : "Gluten-free", "tab" : False, "selectable" : True},
        {"name" : "Nut-free", "tab" : False, "selectable" : True},
        {"name" : "Kid-friendly", "tab" : False, "selectable" : True},
        {"name" : "Breakfast", "tab" : False, "selectable" : True},
        {"name" : "Lunch", "tab" : False, "selectable" : True},
        {"name" : "Dinner", "tab" : False, "selectable" : True},
        {"name" : "Snacks", "tab" : False, "selectable" : True},
    ]

    ingredients = get_all_ingredients()
    
    recipes = get_all_recipes()


    for cat in categories:
        c = add_cat(cat)

    for user in users:
        u = add_user(user)

    for ingredient in ingredients:
        i = add_ingredient(ingredient)

    for recipe in recipes:
        r = add_recipe(recipe)
        

    for c in Category.objects.all():
        print(c)

    for u in User.objects.all():
        print(u)

    for i in Ingredient.objects.all():
        print(i)

    for r in Recipe.objects.all():
        print(r)


def add_ingredient(ingredient):
    i = Ingredient.objects.get_or_create(name=ingredient["name"], ingredient_type = ingredient["ingredient_type"])[0]
    i.save()
    return i

def add_user(user):
    path = "profile_pictures/"
    u = User.objects.get_or_create(username=user["username"], password=user["password"])[0]
    u.set_password(user["password"])
    u.save()
    p = UserProfile.objects.get_or_create(user=u, email=user["email"], profile_picture=path+user["filename"])[0]
    p.save()
    return u

def add_cat(cat):
    c = Category.objects.get_or_create(name=cat["name"], tab=cat["tab"], selectable=cat["selectable"])[0]
    c.save()
    return c

def add_recipe(recipe):
    path = "recipe_pictures/"
    r = Recipe.objects.get_or_create(title=recipe["name"], author=User.objects.get(username=recipe["author"]), steps=recipe["steps"], prep_time=recipe["prep_time"], cook_time=recipe["cook_time"], servings = recipe["servings"], difficulty=recipe["difficulty"], pub_date = recipe["pub_date"], stars = recipe["stars"], picture=path+recipe["filename"])[0]
    for category in recipe["category"]:
        r.category.add(Category.objects.get(name=category))
    for ingredient, properties in recipe["ingredients"].items():
        i = Ingredient.objects.get(name=ingredient)
        r.ingredients.add(i)
        r.save()
        l = IngredientList.objects.get_or_create(recipe=r, ingredient=i)[0]
        l.quantity = properties[0]
        l.plural = properties[1]
        l.save()
    return r

if __name__ == "__main__":
    print("Starting Pantry population script...")
    populate()


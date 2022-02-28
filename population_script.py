import datetime
import os
from pickle import NONE
from random import choices
from tokenize import Name

from django import urls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wad2_team1a_pantry.settings")

import django
django.setup()
from pantry.models import Category, Recipe, SiteUser, Ingredient

def populate():

    siteusers = [
        {"Email" : "johndoe@gmail.com", "Username" : "johndoe", "Password" : "password"},
        {"Email" : "benking@gmail.com", "Username" : "benking", "Password" : "password"},
        {"Email" : "joebloggs@gmail.com", "Username" : "joebloggs", "Password" : "password"},
        {"Email" : "sallywalker@gmail.com", "Username" : "sallywalker", "Password" : "password"}
    ]

    categories = [
        {"Name" : "30 Minute Meals"},
        {"Name" : "Vegan"},
        {"Name" : "Cheap Meals"},
        {"Name" : "Healthy"},
        {"Name" : "Gluten Free"},
        {"Name" : "Vegetarian"},
        {"Name" : "Desserts"},
        {"Name" : "Breakfast"},
        {"Name" : "Lunch"},
        {"Name" : "Dinner"},
        {"Name" : "Snacks"},
    ]

    ingredients = [
        {"Name" : "Cheese", "Type" : "dairy"},
        {"Name" : "Butter", "Type" : "dairy"},
        {"Name" : "Tomatoes", "Type" : "fruit"},
        {"Name" : "Beef", "Type" : "meats"},
        {"Name" : "Ice Cream", "Type" : "sweets"},
        {"Name" : "Biscuits", "Type" : "sweets"},
        {"Name" : "Bread", "Type" : "carbs"},
        {"Name" : "Rice", "Type" : "carbs"},
        {"Name" : "Lettuce", "Type" : "veg"},
        {"Name" : "Water", "Type" : "drinks"},
        {"Name" : "Noodles", "Type" : "carbs"},
        {"Name" : "Spaghetti", "Type" : "carbs"},
        {"Name" : "Flour", "Type" : "carbs"},
        {"Name" : "Eggs", "Type" : "dairy"},
        {"Name" : "Milk", "Type" : "dairy"},
        {"Name" : "Sunflower Oil", "Type" : "fats"},
        {"Name" : "Salt", "Type" : "condiments"},
        {"Name" : "Baby Potatoes", "Type" : "carbs"},
        {"Name" : "Olive Oil", "Type" : "fats"},
        {"Name" : "Red Onions", "Type" : "veg"},
        {"Name" : "Red Peppers", "Type" : "veg"},
        {"Name" : "Garlic", "Type" : "veg"},
        {"Name" : "Sugar", "Type" : "sweets"}

    ]

    
    recipes = [
        {"name":"Halloumi traybake", "author" : "johndoe", "steps" : 
        """
Heat oven to 160C/140C fan/gas 3. Put the potatoes in a large roasting tin with the onion. Pour over 2 tbsp olive oil and roast in the oven for about 30 mins.
Add the chickpeas, pepper, romanesco, tomatoes and garlic. Drizzle with 2 tbsp oil, then roast for a further 20-25 mins until everything is cooked and browning nicely. Toss together briefly and put the halloumi slices on top. Put it under the grill for 5-10 mins, or until the cheese is melting and browning (keep an eye on it). Scatter over the basil leaves to serve.
        """, "ingredients" : ["Baby Potatoes", "Olive Oil", "Red Onions", "Red Peppers", "Garlic"], "category" : ["Vegan", "Healthy", "Vegetarian"], "prep_time" : 15, "cook_time" : 60, "servings" : 4,
         "difficulty" : "medium", "pub_date" : datetime.date(2022,2,27), "stars" : 32},

        {"name":"Pancakes", "author" : "sallywalker", "steps" : 
        """
Put 100g plain flour and a pinch of salt into a large mixing bowl. Make a well in the centre and crack 2 eggs into the middle.
Pour in about 50ml from the 300ml of semi-skimmed milk and 1 tbsp sunflower oil then start whisking from the centre, gradually drawing the flour into the eggs, milk and oil. Once all the flour is incorporated, beat until you have a smooth, thick paste. Add a little more milk if it is too stiff to beat.
Add a good splash of milk and whisk to loosen the thick batter. While still whisking, pour in a steady stream of the remaining milk. Continue pouring and whisking until you have a batter that is the consistency of slightly thick single cream.
Heat the pan over a moderate heat, then wipe it with oiled kitchen paper.
        """, "ingredients" : ["Flour", "Eggs", "Milk", "Sunflower Oil", "Salt"], "category" : ["Vegetarian", "30 Minute Meals", "Cheap Meals"], "prep_time" : 10, "cook_time" : 30, "servings" : 4,
         "difficulty" : "easy", "pub_date" : datetime.date(2022,2,28), "stars" : 64},

         {"name":"New York cheesecake", "author" : "benking", "steps" : 
        """
Position an oven shelf in the middle of the oven. Heat the oven to 180C/ 160C fan/ gas 4.
Line the base of a 23cm springform cake tin by putting a square piece of parchment paper or foil on top of the tin base and then clipping the side on so the paper or foil is trapped and any excess sticks out of the bottom.
        """, "ingredients" : ["Butter", "Biscuits", "Sugar", "Cheese", "Flour"], "category" : ["Vegetarian", "Desserts"], "prep_time" : 20, "cook_time" : 70, "servings" : 12,
         "difficulty" : "hard", "pub_date" : datetime.date(2022,1,13), "stars" : 112}
    ]


    for cat in categories:
        c = add_cat(cat["Name"])

    for user in siteusers:
        u = add_user(user)

    for ingredient in ingredients:
        i = add_ingredient(ingredient)

    for recipe in recipes:
        r = add_recipe(recipe)
        

    for c in Category.objects.all():
        print(c)

    for u in SiteUser.objects.all():
        print(u)

    for i in Ingredient.objects.all():
        print(i)

    for r in Recipe.objects.all():
        print(r)


def add_ingredient(ingredient):
    i = Ingredient.objects.get_or_create(Name=ingredient["Name"], Type = ingredient["Type"])[0]
    i.save()
    return i

def add_user(user):
    c = SiteUser.objects.get_or_create(Username=user["Username"], Email=user["Email"], Password=user["Password"])[0]
    c.save()
    return c

def add_cat(name):
    c = Category.objects.get_or_create(Name=name)[0]
    c.save()
    return c

def add_recipe(recipe):
    r = Recipe.objects.get_or_create(Title=recipe["name"], Author=SiteUser.objects.get(Username=recipe["author"]), Steps=recipe["steps"], PrepTime=recipe["prep_time"], CookTime=recipe["cook_time"], Servings = recipe["servings"], Difficulty=recipe["difficulty"], PubDate = recipe["pub_date"], Stars = recipe["stars"])[0]
    for category in recipe["category"]:
        r.Category.add(Category.objects.get(Name=category))
    for ingredient in recipe["ingredients"]:
        r.Ingredients.add(Ingredient.objects.get(Name=ingredient))
    r.save()
    return r

if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()


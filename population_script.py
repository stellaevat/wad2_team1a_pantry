import datetime
import os

from django import urls

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
        {"name" : "Mains", "tab" : True},
        {"name" : "Appetizers", "tab" : True},
        {"name" : "Desserts", "tab" : True},
        {"name" : "Easy Meals", "tab" : True},
        {"name" : "Under 30'", "tab" : True},
        {"name" : "Vegan", "tab" : False},
        {"name" : "Healthy", "tab" : False},
        {"name" : "GlutenFree", "tab" : False},
        {"name" : "Vegetarian", "tab" : False},
        {"name" : "Breakfast", "tab" : False},
        {"name" : "Lunch", "tab" : False},
        {"name" : "Dinner", "tab" : False},
        {"name" : "Snacks", "tab" : False},
    ]

    ingredients = [
        {"name" : "Cheese", "ingredient_type" : "dairy"},
        {"name" : "Butter", "ingredient_type" : "dairy"},
        {"name" : "Tomatoes", "ingredient_type" : "fruit"},
        {"name" : "Beef", "ingredient_type" : "meats"},
        {"name" : "Ice Cream", "ingredient_type" : "sweets"},
        {"name" : "Biscuits", "ingredient_type" : "sweets"},
        {"name" : "Bread", "ingredient_type" : "carbs"},
        {"name" : "Rice", "ingredient_type" : "carbs"},
        {"name" : "Lettuce", "ingredient_type" : "veg"},
        {"name" : "Water", "ingredient_type" : "drinks"},
        {"name" : "Noodles", "ingredient_type" : "carbs"},
        {"name" : "Spaghetti", "ingredient_type" : "carbs"},
        {"name" : "Flour", "ingredient_type" : "carbs"},
        {"name" : "Eggs", "ingredient_type" : "dairy"},
        {"name" : "Milk", "ingredient_type" : "dairy"},
        {"name" : "Sunflower Oil", "ingredient_type" : "fats"},
        {"name" : "Salt", "ingredient_type" : "condiments"},
        {"name" : "Baby Potatoes", "ingredient_type" : "carbs"},
        {"name" : "Olive Oil", "ingredient_type" : "fats"},
        {"name" : "Red Onions", "ingredient_type" : "veg"},
        {"name" : "Red Peppers", "ingredient_type" : "veg"},
        {"name" : "Garlic", "ingredient_type" : "veg"},
        {"name" : "Sugar", "ingredient_type" : "sweets"}

    ]

    
    recipes = [
        {"name":"Halloumi traybake", "author" : "johndoe", "steps" : 
        """
Heat oven to 160C/140C fan/gas 3. Put the potatoes in a large roasting tin with the onion. Pour over 2 tbsp olive oil and roast in the oven for about 30 mins.
Add the chickpeas, pepper, romanesco, tomatoes and garlic. Drizzle with 2 tbsp oil, then roast for a further 20-25 mins until everything is cooked and browning nicely. Toss together briefly and put the halloumi slices on top. Put it under the grill for 5-10 mins, or until the cheese is melting and browning (keep an eye on it). Scatter over the basil leaves to serve.
        """, "ingredients" : {"Baby Potatoes":"2kg", "Olive Oil":"2 tbsp", "Red Onions":"1", "Red Peppers":"2", "Garlic":"3 cloves"}, "category" : ["Vegan", "Healthy", "Vegetarian"], "prep_time" : 15, "cook_time" : 60, "servings" : 4,
         "difficulty" : "medium", "pub_date" : datetime.date(2022,2,27), "stars" : 32, "filename" : "halloumi-traybake.jpg"},

        {"name":"Pancakes", "author" : "sallywalker", "steps" : 
        """
Put 100g plain flour and a pinch of salt into a large mixing bowl. Make a well in the centre and crack 2 eggs into the middle.
Pour in about 50ml from the 300ml of semi-skimmed milk and 1 tbsp sunflower oil then start whisking from the centre, gradually drawing the flour into the eggs, milk and oil. Once all the flour is incorporated, beat until you have a smooth, thick paste. Add a little more milk if it is too stiff to beat.
Add a good splash of milk and whisk to loosen the thick batter. While still whisking, pour in a steady stream of the remaining milk. Continue pouring and whisking until you have a batter that is the consistency of slightly thick single cream.
Heat the pan over a moderate heat, then wipe it with oiled kitchen paper.
        """, "ingredients" : {"Flour":"100g", "Eggs":"2", "Milk":"300ml", "Sunflower Oil":"1 tbsp", "Salt":"a pinch"}, "category" : ["Vegetarian", "Under 30'", "Easy Meals"], "prep_time" : 10, "cook_time" : 30, "servings" : 4,
         "difficulty" : "easy", "pub_date" : datetime.date(2022,2,28), "stars" : 64, "filename" : "pancakes.jpg"},

         {"name":"New York cheesecake", "author" : "benking", "steps" : 
        """
Position an oven shelf in the middle of the oven. Heat the oven to 180C/ 160C fan/ gas 4.
Line the base of a 23cm springform cake tin by putting a square piece of parchment paper or foil on top of the tin base and then clipping the side on so the paper or foil is trapped and any excess sticks out of the bottom.
        """, "ingredients" : {"Butter":"2 tbsp", "Biscuits":"50g", "Sugar":"1/2 cup", "Cheese":"500g", "Flour":"50g"}, "category" : ["Vegetarian", "Desserts"], "prep_time" : 20, "cook_time" : 70, "servings" : 12,
         "difficulty" : "hard", "pub_date" : datetime.date(2022,1,13), "stars" : 112, "filename" : "new-york-cheesecake.jpg"}
    ]


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
    path = os.getcwd() + "\\media\\profile_pictures\\"
    u = User.objects.get_or_create(username=user["username"], email=user["email"], password=user["password"])[0]
    u.save()
    p = UserProfile.objects.get_or_create(user=u, profile_picture=path+user["filename"])[0]
    p.save()
    return u

def add_cat(cat):
    c = Category.objects.get_or_create(name=cat["name"], tab=cat["tab"])[0]
    c.save()
    return c

def add_recipe(recipe):
    path = os.getcwd() + "\\media\\recipe_pictures\\"
    r = Recipe.objects.get_or_create(title=recipe["name"], author=User.objects.get(username=recipe["author"]), steps=recipe["steps"], prep_time=recipe["prep_time"], cook_time=recipe["cook_time"], servings = recipe["servings"], difficulty=recipe["difficulty"], pub_date = recipe["pub_date"], stars = recipe["stars"], picture=path+recipe["filename"])[0]
    for category in recipe["category"]:
        r.category.add(Category.objects.get(name=category))
    for ingredient, quantity in recipe["ingredients"].items():
        i = Ingredient.objects.get(name=ingredient)
        r.ingredients.add(i)
        r.save()
        l = IngredientList.objects.get_or_create(recipe=r, ingredient=i)[0]
        l.quantity = quantity
        l.save()
    return r

if __name__ == "__main__":
    print("Starting Rango population script...")
    populate()


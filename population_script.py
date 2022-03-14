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
        {"name" : "Tomato", "ingredient_type" : "fruit"},
        {"name" : "Beef", "ingredient_type" : "meats"},
        {"name" : "Ice Cream", "ingredient_type" : "sweets"},
        {"name" : "Biscuit", "ingredient_type" : "sweets"},
        {"name" : "Bread", "ingredient_type" : "carbs"},
        {"name" : "Rice", "ingredient_type" : "carbs"},
        {"name" : "Lettuce", "ingredient_type" : "veg"},
        {"name" : "Water", "ingredient_type" : "drinks"},
        {"name" : "Noodle", "ingredient_type" : "carbs"},
        {"name" : "Spaghetti", "ingredient_type" : "carbs"},
        {"name" : "Flour", "ingredient_type" : "carbs"},
        {"name" : "Egg", "ingredient_type" : "dairy"},
        {"name" : "Milk", "ingredient_type" : "dairy"},
        {"name" : "Sunflower Oil", "ingredient_type" : "fats"},
        {"name" : "Salt", "ingredient_type" : "condiments"},
        {"name" : "Baby Potato", "ingredient_type" : "carbs"},
        {"name" : "Olive Oil", "ingredient_type" : "fats"},
        {"name" : "Red Onion", "ingredient_type" : "veg"},
        {"name" : "Red Pepper", "ingredient_type" : "veg"},
        {"name" : "Garlic", "ingredient_type" : "veg"},
        {"name" : "Sugar", "ingredient_type" : "sweets"},
        {"name" : "Bacon", "ingredient_type" : "meats"},
        {"name" : "Lamb", "ingredient_type" : "meats"},
        {"name" : "Thyme", "ingredient_type" : "herbs"},
        {"name" : "Onion", "ingredient_type" : "veg"},
        {"name" : "Carrot", "ingredient_type" : "veg"},
        {"name" : "Potato", "ingredient_type" : "veg"},
        {"name" : "Lamb Stock", "ingredient_type" : "condiments"},
        {"name" : "Bay Leaf", "ingredient_type" : "herbs"},
        {"name" : "Barley", "ingredient_type" : "herbs"},
        {"name" : "Leek", "ingredient_type" : "veg"},
        {"name" : "Puff Pastry", "ingredient_type" : "carbs"},
        {"name" : "Chicken", "ingredient_type" : "meats"},
        {"name" : "Lemon", "ingredient_type" : "fruit"},
        {"name" : "Green Bean", "ingredient_type" : "veg"},
    ]

    
    recipes = [
        {"name":"Halloumi traybake", "author" : "johndoe", "steps" : 
        """
Heat oven to 160C/140C fan/gas 3. /n Put the potatoes in a large roasting tin with the onion. /n Pour over 2 tbsp olive oil and roast in the oven for about 30 mins. /n
Add the chickpeas, pepper, romanesco, tomatoes and garlic. /n Drizzle with 2 tbsp oil, then roast for a further 20-25 mins until everything is cooked and browning nicely./n Toss together briefly and put the halloumi slices on top./n Put it under the grill for 5-10 mins, or until the cheese is melting and browning (keep an eye on it)./n Scatter over the basil leaves to serve.
        """, "ingredients" : {"Baby Potato":["2kg",True], "Olive Oil":["2 tbsp",False], "Red Onion":["1",False], "Red Pepper":["2",True], "Garlic":["3 cloves",False]}, "category" : ["Vegan", "Healthy", "Vegetarian"], "prep_time" : 15, "cook_time" : 60, "servings" : 4,
         "difficulty" : "medium", "pub_date" : datetime.date(2022,2,27), "stars" : 32, "filename" : "halloumi-traybake.jpg"},

        {"name":"Pancakes", "author" : "sallywalker", "steps" : 
        """
Put 100g plain flour and a pinch of salt into a large mixing bowl./n Make a well in the centre and crack 2 eggs into the middle./n
Pour in about 50ml from the 300ml of semi-skimmed milk and 1 tbsp sunflower oil then start whisking from the centre, gradually drawing the flour into the eggs, milk and oil./n Once all the flour is incorporated, beat until you have a smooth, thick paste./n Add a little more milk if it is too stiff to beat./n
Add a good splash of milk and whisk to loosen the thick batter./n While still whisking, pour in a steady stream of the remaining milk./n Continue pouring and whisking until you have a batter that is the consistency of slightly thick single cream./n
Heat the pan over a moderate heat, then wipe it with oiled kitchen paper.
        """, "ingredients" : {"Flour":["100g",False], "Egg":["2",True], "Milk":["300ml",False], "Sunflower Oil":["1 tbsp",False], "Salt":["a pinch",False]}, "category" : ["Vegetarian", "Under 30'","Desserts", "Easy Meals"], "prep_time" : 10, "cook_time" : 30, "servings" : 4,
         "difficulty" : "easy", "pub_date" : datetime.date(2022,2,28), "stars" : 64, "filename" : "pancakes.jpg"},

         {"name":"New York cheesecake", "author" : "benking", "steps" : 
        """
Position an oven shelf in the middle of the oven. Heat the oven to 180C/ 160C fan/ gas 4./n
Line the base of a 23cm springform cake tin by putting a square piece of parchment paper or foil on top of the tin base and then clipping the side on so the paper or foil is trapped and any excess sticks out of the bottom./n
        """, "ingredients" : {"Butter":["2 tbsp",False], "Biscuit":["50g",True], "Sugar":["1/2 cup",False], "Cheese":["500g",False], "Flour":["50g",False]}, "category" : ["Vegetarian", "Desserts"], "prep_time" : 20, "cook_time" : 70, "servings" : 12,
         "difficulty" : "hard", "pub_date" : datetime.date(2022,1,13), "stars" : 112, "filename" : "new-york-cheesecake.jpg"},

         {"name":"Irish Stew", "author" : "joebloggs", "steps" : 
        """
Heat the slow cooker if necessary, then heat the oil in a frying pan. Sizzle the bacon until crisp, tip into the slow-cooker pot, then brown the chunks of lamb in the pan. Transfer to the slow-cooker pot along with the thyme, onions, carrots, potatoes, stock, bay leaves and enough water to cover the lamb. Cover and cook on Low for 7 hrs./n
Stir in the pearl barley and leek, and cook on High for 1 hr more until the pearl barley is tender./n
Stir in the butter, season and serve scooped straight from the dish.
        """, "ingredients" : {"Butter":["A small knob of",False], "Sunflower Oil":["1 Tbsp",False], "Bacon":["200g",False], "Lamb":["900g",False], "Thyme":["A small bunch of",False], "Onion" : ["3",True], "Carrot" : ["5",True], "Potato" : ["6",True], "Lamb Stock" : ["700ml",False], "Bay Leaf" : ["3",True], "Barley" : ["85g",False], "Leek" : ["1",False]}, "category" : ["Mains", "Easy Meals"], "prep_time" : 20, "cook_time" : 480, "servings" : 6,
         "difficulty" : "hard", "pub_date" : datetime.date(2021,12,25), "stars" : 5, "filename" : "irish-stew.jpg"},

         {"name":"Garlic Chicken Parcels", "author" : "joebloggs", "steps" : 
        """
Heat oven to 220C/200C Fan/gas 7. Cut a slit halfway in each chicken breast, then put each one between two pieces of baking parchment and bash with a rolling pin to flatten slightly./n
Cut your sheet of pastry in half widthways and put both halves on a baking tray. Sit a chicken breast on top of each half, then cram the cavities with the Boursin (don’t worry if a bit of cheese oozes out). Season, scatter over the lemon zest then fold the edges of the pastry in to the centre and pinch shut. Flip each parcel over so the seal is on the bottom. Brush with a little oil, then bake for 30 mins until deep golden./n
About 10 mins before your parcels are ready, steam or boil the greens until tender. Toss in the oil and season. Serve alongside your chicken parcels with lemon wedges for squeezing over.
        """, "ingredients" : {"Chicken":["2 Breasts of",False], "Olive Oil":["1 tbsp",False], "Green Bean":["200g",True], "Garlic":["150g",False], "Puff Pastry":["320g",False], "Lemon" : ["1/2 of a",False]}, "category" : ["Mains", "Easy Meals", "Under 30'"], "prep_time" : 10, "cook_time" : 20, "servings" : 2,
         "difficulty" : "easy", "pub_date" : datetime.date(2021,3,20), "stars" : 60, "filename" : "garlic-chicken-parcels.jpg"}

         
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


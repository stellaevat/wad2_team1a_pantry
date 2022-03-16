import datetime
import os

from django import urls
from datetime import datetime
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
        {"name" : "Bacon", "ingredient_type" : "meats"},
        {"name" : "Lamb", "ingredient_type" : "meats"},
        {"name" : "Beef", "ingredient_type" : "meats"},
        {"name" : "Chicken", "ingredient_type" : "meats"},
        {"name" : "Seitan", "ingredient_type" : "meats"},
        {"name" : "Tempeh", "ingredient_type" : "meats"},
        {"name" : "Vegan sausage", "ingredient_type" : "meats"},
        {"name" : "Chicken breast", "ingredient_type" : "meats"},
        {"name" : "Salmon", "ingredient_type" : "meats"},
        {"name" : "Shrimp", "ingredient_type" : "meats"},
        {"name" : "Cod", "ingredient_type" : "meats"},
        {"name" : "Cheese", "ingredient_type" : "dairy"},
        {"name" : "Butter", "ingredient_type" : "dairy"},
        {"name" : "Egg", "ingredient_type" : "dairy"},
        {"name" : "Milk", "ingredient_type" : "dairy"},
        {"name" : "Parmesan", "ingredient_type" : "dairy"},
        {"name" : "Cream", "ingredient_type" : "dairy"},
        {"name" : "Goat cheese", "ingredient_type" : "dairy"},
        {"name" : "Oat milk", "ingredient_type" : "dairy"},
        {"name" : "Almond milk", "ingredient_type" : "dairy"},
        {"name" : "Soy milk", "ingredient_type" : "dairy"},
        {"name" : "Cashew milk", "ingredient_type" : "dairy"},
        {"name" : "Plain yoghurt", "ingredient_type" : "dairy"},
        {"name" : "Greek yoghurt", "ingredient_type" : "dairy"},
        {"name" : "Cheddar", "ingredient_type" : "dairy"},
        {"name" : "Tomato", "ingredient_type" : "veg"},
        {"name" : "Lettuce", "ingredient_type" : "veg"},
        {"name" : "Onion", "ingredient_type" : "veg"},
        {"name" : "Carrot", "ingredient_type" : "veg"},
        {"name" : "Potato", "ingredient_type" : "veg"},
        {"name" : "Red onion", "ingredient_type" : "veg"},
        {"name" : "Red pepper", "ingredient_type" : "veg"},
        {"name" : "Baby potato", "ingredient_type" : "veg"},
        {"name" : "Green bean", "ingredient_type" : "veg"},
        {"name" : "Leek", "ingredient_type" : "veg"},
        {"name" : "Avocado", "ingredient_type" : "veg"},
        {"name" : "Arugula", "ingredient_type" : "veg"},
        {"name" : "Belunga lentil", "ingredient_type" : "pulses"},
        {"name" : "Green lentil", "ingredient_type" : "pulses"},
        {"name" : "Kidney bean", "ingredient_type" : "pulses"},
        {"name" : "Black bean", "ingredient_type" : "pulses"},
        {"name" : "Black eyed bean", "ingredient_type" : "pulses"},
        {"name" : "Chickpea", "ingredient_type" : "pulses"},
        {"name" : "Green pea", "ingredient_type" : "pulses"},
        {"name" : "Quinoa", "ingredient_type" : "grains"},
        {"name" : "Barley", "ingredient_type" : "grains"},
        {"name" : "Walnut", "ingredient_type" : "grains"},
        {"name" : "Bulgur wheat", "ingredient_type" : "grains"},
        {"name" : "Rye", "ingredient_type" : "grains"},
        {"name" : "Cashew", "ingredient_type" : "grains"},
        {"name" : "Almond", "ingredient_type" : "grains"},
        {"name" : "Peanut", "ingredient_type" : "grains"},
        {"name" : "Walnut", "ingredient_type" : "grains"},
        {"name" : "Bread", "ingredient_type" : "carbs"},
        {"name" : "Rice", "ingredient_type" : "carbs"},
        {"name" : "Noodle", "ingredient_type" : "carbs"},
        {"name" : "Spaghetti", "ingredient_type" : "carbs"},
        {"name" : "Ciabatta loaf", "ingredient_type" : "carbs"},
        {"name" : "Pasta", "ingredient_type" : "carbs"},
        {"name" : "Wholewheat bread", "ingredient_type" : "carbs"},
        {"name" : "Tagliatelle", "ingredient_type" : "carbs"},
        {"name" : "Spaghetti", "ingredient_type" : "carbs"},
        {"name" : "Wild rice", "ingredient_type" : "carbs"},
        {"name" : "Brown rice", "ingredient_type" : "carbs"},
        {"name" : "Burger bun", "ingredient_type" : "carbs"},
        {"name" : "Sunflower oil", "ingredient_type" : "fats"},
        {"name" : "Olive oil", "ingredient_type" : "fats"},
        {"name" : "Lard", "ingredient_type" : "fats"},
        {"name" : "Avocado oil", "ingredient_type" : "fats"},
        {"name" : "Sesame oil", "ingredient_type" : "fats"},
        {"name" : "Duck fat", "ingredient_type" : "fats"},
        {"name" : "Thyme", "ingredient_type" : "herbs"},
        {"name" : "Salt", "ingredient_type" : "herbs"},
        {"name" : "Garlic", "ingredient_type" : "herbs"},
        {"name" : "Bay leaf", "ingredient_type" : "herbs"},
        {"name" : "Parsley", "ingredient_type" : "herbs"},
        {"name" : "Sage", "ingredient_type" : "herbs"},
        {"name" : "Paprika", "ingredient_type" : "herbs"},
        {"name" : "Turmeric", "ingredient_type" : "herbs"},
        {"name" : "Rosemary", "ingredient_type" : "herbs"},
        {"name" : "Thyme", "ingredient_type" : "herbs"},
        {"name" : "Italian seasoning", "ingredient_type" : "herbs"},
        {"name" : "Oregano", "ingredient_type" : "herbs"},
        {"name" : "Cumin", "ingredient_type" : "herbs"},
        {"name" : "Cinammon", "ingredient_type" : "herbs"},
        {"name" : "Lamb stock", "ingredient_type" : "condiments"},
        {"name" : "Honey mustard vinaigrette", "ingredient_type" : "condiments"},
        {"name" : "Soy sauce", "ingredient_type" : "condiments"},
        {"name" : "Ketchup", "ingredient_type" : "condiments"},
        {"name" : "Tomato passata", "ingredient_type" : "condiments"},
        {"name" : "Mayonaise", "ingredient_type" : "condiments"},
        {"name" : "Mustard", "ingredient_type" : "condiments"},
        {"name" : "Sauerkraut", "ingredient_type" : "condiments"},
        {"name" : "Lemon", "ingredient_type" : "fruit"},
        {"name" : "Cranberry", "ingredient_type" : "fruit"},
        {"name" : "Orange", "ingredient_type" : "fruit"},
        {"name" : "Granny smith apple", "ingredient_type" : "fruit"},
        {"name" : "Red apple", "ingredient_type" : "fruit"},
        {"name" : "Banana", "ingredient_type" : "fruit"},
        {"name" : "Strawberry", "ingredient_type" : "fruit"},
        {"name" : "Blueberry", "ingredient_type" : "fruit"},
        {"name" : "Grapefruit", "ingredient_type" : "fruit"},
        {"name" : "Lime", "ingredient_type" : "fruit"},
        {"name" : "Pomelo", "ingredient_type" : "fruit"},
        {"name" : "Flour", "ingredient_type" : "baking"},
        {"name" : "Ice cream", "ingredient_type" : "baking"},
        {"name" : "Biscuit", "ingredient_type" : "baking"},
        {"name" : "Sugar", "ingredient_type" : "baking"},
        {"name" : "Puff pastry", "ingredient_type" : "baking"},
        {"name" : "Vanilla extract", "ingredient_type" : "baking"},
        {"name" : "Baking powder", "ingredient_type" : "baking"},
        {"name" : "Brown sugar", "ingredient_type" : "baking"},
        {"name" : "Maple syrup", "ingredient_type" : "baking"},
        {"name" : "Honey", "ingredient_type" : "baking"},
        {"name" : "Agave", "ingredient_type" : "baking"},
        {"name" : "Self-rising flour", "ingredient_type" : "baking"},
        {"name" : "Wholewheat flour", "ingredient_type" : "baking"},
        {"name" : "Cornmeal", "ingredient_type" : "baking"},
        {"name" : "Cornmeal", "ingredient_type" : "baking"},
        {"name" : "Oatmeal", "ingredient_type" : "baking"},
        {"name" : "Water", "ingredient_type" : "drinks"},
        {"name" : "Red wine", "ingredient_type" : "drinks"},  
        {"name" : "White wine", "ingredient_type" : "drinks"},  
        {"name" : "Beer", "ingredient_type" : "drinks"},  
        {"name" : "Orange juice", "ingredient_type" : "drinks"},  
        {"name" : "Apple juice", "ingredient_type" : "drinks"},  
        {"name" : "Ice", "ingredient_type" : "drinks"},  
        {"name" : "Whiskey", "ingredient_type" : "drinks"},
        {"name" : "Brandy", "ingredient_type" : "drinks"},
        {"name" : "Gin", "ingredient_type" : "drinks"},  
        {"name" : "Coffee", "ingredient_type" : "drinks"},
        {"name" : "Espresso", "ingredient_type" : "drinks"}, 
        {"name" : "Matcha tea", "ingredient_type" : "drinks"},
        {"name" : "Green tea", "ingredient_type" : "drinks"},       
        {"name" : "Dark tea", "ingredient_type" : "drinks"},
        {"name" : "Chamomile tea", "ingredient_type" : "drinks"},
    ]

    
    recipes = [
        {"name":"Halloumi traybake", "author" : "johndoe", "steps" : 
        """Heat oven to 160C/140C fan/gas 3.
Put the potatoes in a large roasting tin with the onion.
Pour over 2 tbsp olive oil and roast in the oven for about 30 mins.
Add the chickpeas, pepper, romanesco, tomatoes and garlic.
Drizzle with 2 tbsp oil, then roast for a further 20-25 mins until everything is cooked and browning nicely.
Toss together briefly and put the halloumi slices on top.
Put it under the grill for 5-10 mins, or until the cheese is melting and browning (keep an eye on it).
Scatter over the basil leaves to serve.""", "ingredients" : {"Baby potato":["2kg",True], "Olive oil":["2 tbsp",False], "Red onion":["1",False], "Red pepper":["2",True], "Garlic":["3 cloves",False]}, "category" : ["Mains", "Healthy", "Vegetarian"], "prep_time" : 15, "cook_time" : 60, "servings" : 4,
         "difficulty" : "medium", "pub_date" : datetime(2022,2,27,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 32, "filename" : "halloumi-traybake.jpg"},

        {"name":"Pancakes", "author" : "sallywalker", "steps" : 
        """Put 100g plain flour and a pinch of salt into a large mixing bowl. Make a well in the centre and crack 2 eggs into the middle.
Pour in about 50ml from the 300ml of semi-skimmed milk and 1 tbsp sunflower oil then start whisking from the centre, gradually drawing the flour into the eggs, milk and oil.
Once all the flour is incorporated, beat until you have a smooth, thick paste. Add a little more milk if it is too stiff to beat.
Add a good splash of milk and whisk to loosen the thick batter. While still whisking, pour in a steady stream of the remaining milk.Continue pouring and whisking until you have a batter that is the consistency of slightly thick single cream.
Heat the pan over a moderate heat, then wipe it with oiled kitchen paper.""", "ingredients" : {"Flour":["100g",False], "Egg":["2",True], "Milk":["300ml",False], "Sunflower oil":["1 tbsp",False], "Salt":["a pinch",False]}, "category" : ["Vegetarian", "Desserts", "Easy Meals"], "prep_time" : 10, "cook_time" : 30, "servings" : 4,
         "difficulty" : "easy", "pub_date" : datetime(2022,2,28,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 64, "filename" : "pancakes.jpg"},

         {"name":"New York cheesecake", "author" : "benking", "steps" : 
        """Position an oven shelf in the middle of the oven. Heat the oven to 180C/ 160C fan/ gas 4.
Line the base of a 23cm springform cake tin by putting a square piece of parchment paper or foil on top of the tin base and then clipping the side on so the paper or foil is trapped and any excess sticks out of the bottom.""", "ingredients" : {"Butter":["2 tbsp",False], "Biscuit":["50g",True], "Sugar":["1/2 cup",False], "Cheese":["500g",False], "Flour":["50g",False]}, "category" : ["Vegetarian", "Desserts"], "prep_time" : 20, "cook_time" : 70, "servings" : 12,
         "difficulty" : "hard", "pub_date" : datetime(2022,1,13,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 112, "filename" : "new-york-cheesecake.jpg"},

         {"name":"Irish Stew", "author" : "joebloggs", "steps" : 
        """Heat the slow cooker if necessary, then heat the oil in a frying pan. Sizzle the bacon until crisp, tip into the slow-cooker pot, then brown the chunks of lamb in the pan. Transfer to the slow-cooker pot along with the thyme, onions, carrots, potatoes, stock, bay leaves and enough water to cover the lamb. Cover and cook on Low for 7 hrs.
Stir in the pearl barley and leek, and cook on High for 1 hr more until the pearl barley is tender.
Stir in the butter, season and serve scooped straight from the dish.""", "ingredients" : {"Butter":["A small knob of",False], "Sunflower oil":["1 Tbsp",False], "Bacon":["200g",False], "Lamb":["900g",False], "Thyme":["A small bunch of",False], "Onion" : ["3",True], "Carrot" : ["5",True], "Potato" : ["6",True], "Lamb stock" : ["700ml",False], "Bay leaf" : ["3",True], "Barley" : ["85g",False], "Leek" : ["1",False]}, "category" : ["Mains", "Easy Meals"], "prep_time" : 20, "cook_time" : 480, "servings" : 6,
         "difficulty" : "hard", "pub_date" : datetime(2021,12,25,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 5, "filename" : "irish-stew.jpg"},

         {"name":"Garlic Chicken Parcels", "author" : "joebloggs", "steps" : 
        """Heat oven to 220C/200C Fan/gas 7. Cut a slit halfway in each chicken breast, then put each one between two pieces of baking parchment and bash with a rolling pin to flatten slightly.
Cut your sheet of pastry in half widthways and put both halves on a baking tray. Sit a chicken breast on top of each half, then cram the cavities with the Boursin. Season, scatter over the lemon zest then fold the edges of the pastry in to the centre and pinch shut. Flip each parcel over so the seal is on the bottom. Brush with a little oil, then bake for 30 mins until deep golden.
About 10 mins before your parcels are ready, steam or boil the greens until tender. Toss in the oil and season. Serve alongside your chicken parcels with lemon wedges for squeezing over.""", "ingredients" : {"Chicken breast":["2",True], "Olive oil":["1 tbsp",False], "Green bean":["200g",True], "Garlic":["150g",False], "Puff pastry":["320g",False], "Lemon" : ["1/2 of a",False]}, "category" : ["Mains", "Easy Meals", "Under 30'"], "prep_time" : 10, "cook_time" : 20, "servings" : 2,
         "difficulty" : "easy", "pub_date" : datetime(2021,3,20,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 60, "filename" : "garlic-chicken-parcels.jpg"},

         {"name":"Pasta", "author" : "benking", "steps" : 
        """Heat a pot of saltwater big enough to accommodate your cooked pasta plus an inch or two of pasta water (for a pound of pasta, you'll want four quarts).
When it's boiling (you'll see big bubbles in the water and steam rising from the pot), add your pasta
After it comes to a boil again, set a timer to the minutes specified on the pasta box, adjusting the flame downward if it begins boiling over, which sometimes happens.
When the timer goes off, drain and rinse the pasta in cool water to stop the cooking process.""", "ingredients" : {"Pasta":["500g",False], "Water":["1 Litre",False]}, "category" : ["Mains", "Easy Meals", "Under 30'", "Vegan"], "prep_time" : 2, "cook_time" : 10, "servings" : 1,
         "difficulty" : "easy", "pub_date" : datetime(2022,3,14,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 500, "filename" : "pasta.jpg"},

         {"name":"Omelet", "author" : "sallywalker", "steps" : 
        """Whisk together the eggs and heavy cream in a small bowl.
Heat a non-stick pan over medium heat. Melt the butter on the pan.
Pour in the egg mixture and cook the eggs for 1 to 2 minutes—or until the eggs are halfway cooked.
Place your desired fillings in the middle of the omelet.
Using a spatula, fold the omelet in half. Cook for another 30 seconds, then slide the omelet to a plate. Serve immediately.""", "ingredients" : {"Egg":["2",True], "Cream":["1 tbsp",False], "Butter" : ["1/2 tbsp", False]}, "category" : ["Mains", "Easy Meals", "Under 30'", "Breakfast"], "prep_time" : 5, "cook_time" : 5, "servings" : 1,
         "difficulty" : "medium", "pub_date" : datetime(2022,3,14,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 22, "filename" : "omelet.jpg"},

         {"name":"Grilled Chicken and Avocado Salad", "author" : "johndoe", "steps" : 
        """Combine the chicken, arugula, cranberries, avocado, goat cheese, walnuts, vinaigrette, salt, and pepper in a large bowl, using your hands or 2 forks to fully incorporate the dressing.""", "ingredients" : {"Chicken":["12 Oz",False], "Arugula":["12 Cups",False], "Cranberry" : ["1/4 cup", True], "Avocado":["1",False], "Goat cheese":["1/4",False], "Walnut":["1/4 Cup",True], "Honey mustard vinaigrette":["1/4 Cup",False]}, "category" : ["Mains", "Easy Meals", "Vegan", "Vegetarian", "Lunch"], "prep_time" : 5, "cook_time" : 0, "servings" : 4,
         "difficulty" : "easy", "pub_date" : datetime(2022,2,14,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 50, "filename" : "grilled-chicken-and-avocado-salad.jpg"},

         {"name":"Garlic Bread Toasts", "author" : "joebloggs", "steps" : 
        """Slice the bread in half lengthwise. Toast the crust side for 2 mins until really crispy. Mix together butter, garlic and parsley in a bowl. Spread over the cut bread halves. Sprinkle over the Parmesan. Just before serving place on a baking sheet, then cook under a hot grill for 5 mins until toasty and lightly golden. Let it cool for 1 min before cutting into thick slices.""", "ingredients" : {"Ciabatta loaf":["2",True], "Butter":["140g",False], "Garlic" : ["4-6 Cloves", False], "Parsley":["A Handful of",False], "Parmesan":["2 tbsp",False]}, "category" : ["Appetizers", "Easy Meals", "Under 30'", "Vegetarian", "Lunch", "Dinner","Snacks"], "prep_time" : 10, "cook_time" : 7, "servings" : 12,
         "difficulty" : "easy", "pub_date" : datetime(2022,2,1,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 77, "filename" : "garlic-bread-toasts.jpg"},

         {"name":"Grilled & Roasted Potatoes", "author" : "sallywalker", "steps" : 
        """Preheat the oven to 200°C/400°F/gas 6. Roast the potatoes, uncovered, for 45 minutes on the top shelf, or until cooked through and lightly golden. Squeeze the soft garlic cloves out of their skins, to serve.""", "ingredients" : {"Sage":["1 Bunch",False], "Lemon":["1.5",True], "Garlic" : ["1 Bulb", False], "Olive oil":["1 tbsp",False]}, "category" : ["Appetizers", "Easy Meals", "GlutenFree", "Vegetarian", "Lunch", "Dinner","Snacks"], "prep_time" : 10, "cook_time" : 45, "servings" : 6,
         "difficulty" : "easy", "pub_date" : datetime(2022,1,1,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 10, "filename" : "grilled-and-roasted-potatoes.jpg"},

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
    u.set_password(user["password"])
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


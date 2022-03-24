from datetime import datetime
import pytz

recipes = [
        {"name":"Halloumi traybake", "author" : "johndoe", "steps" : 
        """Heat oven to 160C/140C fan/gas 3.
Put the potatoes in a large roasting tin with the onion.
Pour over 2 tbsp olive oil and roast in the oven for about 30 mins.
Add the chickpeas, pepper, romanesco, tomatoes and garlic.
Drizzle with 2 tbsp oil, then roast for a further 20-25 mins until everything is cooked and browning nicely.
Toss together briefly and put the halloumi slices on top.
Put it under the grill for 5-10 mins, or until the cheese is melting and browning (keep an eye on it).
Scatter over the basil leaves to serve.""", "ingredients" : {"Baby potato":["2kg",True], "Olive oil":["2 tbsp",False], "Red onion":["1",False], "Red pepper":["2",True], "Garlic":["3 cloves",False]}, "category" : ["Mains", "Healthy", "Vegetarian"],
        "prep_time" : 15, "cook_time" : 60, "servings" : 4,
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

         {"name":"Grilled Potato and Avocado Salad", "author" : "johndoe", "steps" : 
        """Combine the Potato, arugula, cranberries, avocado, goat cheese, walnuts, honey mustard vinaigrette, salt, and pepper in a large bowl, using your hands or 2 forks to fully incorporate the dressing.""", "ingredients" : {"Potato":["12 Oz",True], "Arugula":["12 Cups",False], "Cranberry" : ["1/4 cup", True], "Avocado":["1",False], "Goat cheese":["1/4",False], "Walnut":["1/4 Cup",True], "Honey mustard":["1/4 Cup",False]}, "category" : ["Mains", "Easy Meals", "Vegan", "Vegetarian", "Lunch"], "prep_time" : 5, "cook_time" : 0, "servings" : 4,
         "difficulty" : "easy", "pub_date" : datetime(2022,2,14,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 50, "filename" : "grilled-potato-and-avocado-salad.jpg"},

         {"name":"Garlic Bread Toasts", "author" : "joebloggs", "steps" : 
        """Slice the bread in half lengthwise. Toast the crust side for 2 mins until really crispy. Mix together butter, garlic and parsley in a bowl. Spread over the cut bread halves. Sprinkle over the Parmesan. Just before serving place on a baking sheet, then cook under a hot grill for 5 mins until toasty and lightly golden. Let it cool for 1 min before cutting into thick slices.""", "ingredients" : {"Ciabatta loaf":["2",True], "Butter":["140g",False], "Garlic" : ["4-6 Cloves", False], "Parsley":["A Handful of",False], "Parmesan":["2 tbsp",False]}, "category" : ["Appetizers", "Easy Meals", "Under 30'", "Vegetarian", "Lunch", "Dinner","Snacks"], "prep_time" : 10, "cook_time" : 7, "servings" : 12,
         "difficulty" : "easy", "pub_date" : datetime(2022,2,1,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 77, "filename" : "garlic-bread-toasts.jpg"},

         {"name":"Grilled & Roasted Potatoes", "author" : "sallywalker", "steps" : 
        """Preheat the oven to 200°C/400°F/gas 6. Roast the potatoes, uncovered, for 45 minutes on the top shelf, or until cooked through and lightly golden. Squeeze the soft garlic cloves out of their skins, to serve.""", "ingredients" : {"Sage":["1 Bunch",False], "Lemon":["1.5",True], "Garlic" : ["1 Bulb", False], "Olive oil":["1 tbsp",False]}, "category" : ["Appetizers", "Easy Meals", "Gluten-free", "Vegetarian", "Lunch", "Dinner","Snacks"], "prep_time" : 10, "cook_time" : 45, "servings" : 6,
         "difficulty" : "easy", "pub_date" : datetime(2022,1,1,20,9,26,423063,tzinfo=pytz.UTC), "stars" : 10, "filename" : "grilled-and-roasted-potatoes.jpg"},
        {"name":"Spanish Lentils", "author":"johndoe",
        "steps":"""Dice one of the onions. Boil it and the lentils at medium heat, for one hour.
While the lentils cook, dice the rest of the onions, the garlic, the tomatoes and the green pepper.
Fry the diced onion, garlic and pepper on a pan. After 10 minutes, add the sausage in slices. 5 minutes later, add the tomato and cook for a further 10 minutes at medium heat.
In the meantime, peel the potatoes and carrots, and cut them into medium chunks.
Once the lentils have been cooking for around 30 minutes, add the carrots and potatoes, as well as everything in the frying pan. Cook everything in the pot until the lentils, potatoes and carrots are soft.
Serve or refrigerate for another day. If you liked this recipe, please star it and share it!""",
        "ingredients" : {"Brown lentil":["400g",False], "Onion":["2",True], "Tomato":["4",True], "Garlic":["4",True], "Green pepper":["1",False], "Pork sausage":["200g",False], "Carrot":["2",True], "Potato":["2",True]},
        "category" : ["Mains", "Lunch", "Dinner", "Nut-free"],
        "prep_time" : 15, "cook_time" : 60, "servings" : 4, "difficulty" : "medium", "pub_date" : datetime(2022,2,15,10,34,45,0,tzinfo=pytz.UTC), "stars" : 357, "filename" : "spanish-lentils.png"},
         
        {"name":"Russian Dressing", "author":"joebloggs",
        "steps":"""A true classic, popularized by Tim R. Heidecker at the start of the 2010s. Goes great with salads and Reuben sandwiches among many others.
Combine the mayonnaise with the ketchup and mix.
Keep mixing.
Mix until the mix is spilling out of the bowl.
Add the mustard. I personally recommend Pissman's Mustard but I have to admit they paid me to write this recipe. Add a whole bottle if you want -- you can't go wrong!
Some of the mixture should have spilled all over the counter: this is intended. Scoop the spillage back into the bowl -- use your hands for maximum flavour!
Serve with salad, or use in a sandwich for added flavour!""",
        "ingredients" : {"Mayonnaise":["50g",False], "Ketchup":["45g",False], "Mustard":["50g",False]},
        "category" : ["Under 30'", "Vegan", "Nut-free", "Vegetarian", "Snacks", "Appetizers"],
        "prep_time" : 5, "cook_time" : 5, "servings" : 10, "difficulty" : "easy", "pub_date" : datetime(2021,1,28,12,23,47,0,tzinfo=pytz.UTC), "stars" : 3, "filename" : "russian-dressing.jpg"},
		 
		{"name":"Mexican omelette", "author":"sallywalker",
        "steps":"""Whisk eggs, milk, 1/4 cup cheese and salt and pepper in a jug. Combine onion, parsley and remaining 1/2 cup cheese in a bowl.
Heat half the butter and half the oil in a 19cm (base) non-stick frying pan over high heat until sizzling. Reduce heat to medium-low. Pour in half the egg mixture. Cook for 2 to 3 minutes or until egg starts to set.
Cook for 3 to 4 minutes or until egg is golden and set. Roll up omelette. Slide onto a plate. Repeat with remaining butter, oil, egg mixture and capsicum mixture. Serve.""",
        "ingredients" : {"Egg":["4",True], "Milk":["1/3 cups",False], "Cheese":["3/4 cup",False], "Onion":["4",True], "Parsley":["1/4 cup leaves",False], "Butter":["20g",False], "Olive oil":["3/4 cup",False]},
        "category" : ["Under 30'", "Vegetarian", "Snacks", "Breakfast", "Lunch", "Dinner"],
        "prep_time" :10, "cook_time" : 15, "servings" : 2, "difficulty" : "easy", "pub_date" : datetime(2019,4,16,17,23,47,0,tzinfo=pytz.UTC), "stars" : 94, "filename" : "mexican-omelette.jpeg"},
		 
		{"name":"Two-tone chocolate tart", "author":"benking",
        "steps":"""FOR PASTRY: Process flour, sugar and butter until mixture resembles fine breadcrumbs.
Add egg yolk. Process until mixture just comes together.
Turn onto a lightly floured surface. Knead until just smooth. Shape into a disc.
Cover in plastic wrap. Refrigerate for 20 minutes.
Preheat oven to 180°C/160°C fan-forced.
Grease two 3cm-deep, 10.5cm (base) round fluted, loose-based tart pans. Roll pastry out between 2 sheets of baking paper until 3mm thick.
Using a 12cm round cutter, cut 2 rounds from pastry.
Line prepared pans with pastry. Trim excess. Refrigerate for 10 minutes or until firm.
Place pans on a baking tray. Line pastry cases with baking paper. Fill with ceramic pie weights or uncooked rice.
Bake for 10 minutes or until edges are golden. Remove paper and weights or rice. Bake for 5 minutes or until golden.
FOR FILLING: Reduce oven to 160°C/140°C fan-forced. Combine dark chocolate and butter in a saucepan over low heat. Cook, stirring, for 2 minutes or until smooth.
Using an electric mixer, beat egg, egg yolk and sugar until light and fluffy.
Fold chocolate mixture into egg mixture. Pour into pastry cases.
Bake for 10 minutes or until just set.
Cool for 10 minutes. Refrigerate for 30 minutes or until firm.
Meanwhile, combine white chocolate and cream in a saucepan over low heat.Cook, stirring, for 3 minutes or until smooth.
Cool for 20 minutes. Spread white chocolate mixture over dark chocolate mixture.
Refrigerate for 1 hour or until set. Serve topped with raspberries.""",
        "ingredients" : {"Dark chocolate":["65g",False],"Butter":["115g",False],"Egg":["2",True],"Sugar":["3 tbsp",False],"White chocolate":["65g",False],"Cream":["2 tbsp",False],"Raspberry":["2",True],"Flour":["2/3 cup",False]},
        "category" : ["Desserts", "Kid-friendly"], "prep_time" :160, "cook_time" : 25,"servings" : 2, "difficulty" : "advanced", "pub_date" : datetime(2021,5,7,9,15,47,0,tzinfo=pytz.UTC),"stars" : 15,"filename" : "two-tone-chocolate-tart.jpg"},
		 
		{"name":"Tomato bisque", "author":"benking",
        "steps":"""In a small bowl mix flour with salt, pepper and garlic. Add eggs to a second small bowl and finally add panko to a third small bowl.
Start by prepping the fried cheese. Working with one square at a time dip the cheese into the egg mixture followed by the flour mixture, then back into the egg mixture and finally into the panko. Set cheese on a lined baking sheet and repeat with remaining cheese. Place in freezer and freeze for 30 minutes.
In a 5qt pot melt butter over medium heat. Add in carrots and onions and stir until onions are translucent. Add in tomatoes, olive oil, bay leaves, salt and pepper.
Bring soup to a boil and reduce to a simmer. Allow to cook for 30 minutes. Add in fresh basil and remove from heat.""",
        "ingredients" : {"Butter":["4tbsp",False],"Carrot":["2",True],"Tomato":["28oz, diced",True],"Onion":["1",False],"Bay leaf":["2",True],"Olive oil":["1/3 cup",False],"Salt":["2 tsp",False],"Black pepper":["1/2 tsp",False],"Cream":["1 cup",False],},
        "category" : ["Under 30'", "Vegetarian", "Snacks", "Breakfast", "Lunch", "Dinner"],
        "prep_time" :45, "cook_time" : 45, "servings" : 6, "difficulty" : "medium", "pub_date" : datetime(2019,4,16,17,23,47,0,tzinfo=pytz.UTC), "stars" : 105,"filename" : "tomato-bisque.jpg"},

        {"name":"Creamy pulse dhal", "author":"johndoe",
        "steps":"""Combine lentils and split peas in a medium-large pot and cover with 4cm of water. Add the kidney beans. Bring to a boil and simmer over low heat, stirring occasionally, until the lentils and split peas are tender and the water has absorbed (about 30 minutes).
While pulses are cooking, heat the oil over medium heat in a large frying pan. When shimmering add cumin seeds and cook just until they darken (30-60 seconds).
Add the onion and garlic and cook, stirring frequently, until golden brown (15 minutes). Add the ground coriander, turmeric and cayenne and cook, stirring a few times, until fragrant (2 minutes). Add the tomatoes and simmer for 5 minutes. Add to the cooked pulses, stir to combine and simmer over low heat for another 5 minutes.
Stir in salt and pepper. (The dhal can be made ahead and chilled for up to five days. Reheat gently, adding water as necessary if it is too thick.) Just before serving, stir in the coriander leaves.""",
        "ingredients" : {"Red lentil":["3/4 cup",True],"Chickpea":["3/4 cup",True],"Kidney bean":["400g",True],"Olive oil":["3 tbsp",False],"Onion":["1",False],"Tomato":["1 can, chopped",True],"Garlic":["2 cloves, crushed",True],"Cayenne pepper":["1/2 tsp",False],"Turmeric":["1 tsp",False],"Salt":["1 tsp",False],},
        "category" : ["Mains", "Lunch", "Dinner", "Nut-free"],
        "prep_time" : 10,"cook_time" : 60,"servings" : 6,"difficulty" : "advanced","pub_date" : datetime(2012,2,15,10,34,45,0,tzinfo=pytz.UTC),"stars" : 86,"filename" : "creamy-pulse-dhal.jpg"},
		 
		{"name":"Avocado and quinoa salad","author":"joebloggs",
        "steps":"""Rinse the quinoa under cold water. Tip into a saucepan, cover with water and bring to the boil. Reduce the heat and simmer for 15 mins until the grains have swollen but still have some bite. Drain, then transfer to a bowl to cool slightly.
Meanwhile, in a jug, combine the oil, lemon juice and vinegar with some seasoning.
Once the quinoa has cooled, mix with the dressing and all the remaining ingredients and season. Divide between plates or lunchboxes.""",
        "ingredients" : {"Quinoa":["100g",False],"Olive oil":["3 tbsp",False],"Avocado":["1",False],"Garlic":["2 cloves, crushed",True],"Turmeric":["1 tsp",False],"Salt":["1 tsp",False],},
        "category" : ["Mains", "Lunch", "Dinner", "Nut-free"],
        "prep_time" : 5,"cook_time" : 20,"servings" : 6,"difficulty" : "easy","pub_date" : datetime(2022,2,13,10,34,45,0,tzinfo=pytz.UTC),"stars" : 5,"filename" : "avocado-and-quinoa-salad.jpeg"},
		 
		{"name":"Kidney bean curry","author":"joebloggs",
        "steps":"""Heat the oil in a large frying pan over a low-medium heat. Add the onion and a pinch of salt and cook slowly, stirring occasionally, until softened and just starting to colour. Add the garlic, ginger and coriander stalks and cook for a further 2 mins, until fragrant.
Add the spices to the pan and cook for another 1 min, by which point everything should smell aromatic. Tip in the chopped tomatoes and kidney beans in their water, then bring to the boil.
Turn down the heat and simmer for 15 mins until the curry is nice and thick. Season to taste, then serve with the basmati rice and the coriander leaves.""",
        "ingredients" : {"Onion":["1",False],"Kidney bean":["400g",True],"Olive oil":["3 tbsp",False],"Tomato":["1 can, chopped",True],"Garlic":["2 cloves, crushed",True],"Turmeric":["1 tsp",False],"Salt":["1 tsp",False],},
        "category" : ["Mains", "Lunch", "Dinner",],
        "prep_time" : 10,"cook_time" : 40,"servings" : 4,"difficulty" : "easy","pub_date" : datetime(2019,2,11,10,34,45,0,tzinfo=pytz.UTC),"stars" : 85,"filename" : "kidney-bean-curry.jpg"},
		 
		{"name":"Mixed bean chilli with wedges","author":"sallywalker",
        "steps":"""Heat oven to 220C/200C fan/gas 7. Toss the potato wedges in 2 tsp oil and spread out in a single layer on a large baking tray. Cook for 30-35 mins, turning halfway, until tender and golden brown.
Meanwhile, for the chilli, put the remaining oil into a casserole dish and fry the onion and pepper for 5 mins. Add Cajun spice, pulses, tomatoes and stock. Cover and simmer for 15-20 mins. Remove casserole from the heat and stir in the chocolate until melted. Ladle the chilli into bowls, top each with 1 tbsp soured cream and serve with the wedges.""",
        "ingredients" : {"Onion":["1",False],"Potato":["4",True],"Kidney bean":["200g",True],"Pinto bean":["200g",True],"Black bean":["50g",True],"Olive oil":["4 tbsp",False],"Tomato":["1 can, chopped",True],"Garlic":["2 cloves, crushed",True],"Dark chocolate":["1tbsp chopped",False],"Cream":["4tbsp",False],},
        "category" : ["Mains", "Lunch", "Dinner",],"prep_time" : 10,"cook_time" : 40,"servings" : 4,"difficulty" : "easy","pub_date" : datetime(2020,2,11,14,46,45,0,tzinfo=pytz.UTC),"stars" : 85,"filename" : "mixed-bean-chilli-with-wedges.jpg"},
		
		{"name":"Spiced mushroom and lentil hotpot","author":"joebloggs",
        "steps":"""Heat oven to 200C/180C fan/gas 6.
Heat half the oil in a medium saucepan. Fry the onion for 3 mins, then add the mushrooms. Cook for another 3 mins, then increase the heat and add the garlic, ground cumin and paprika, and cook for 1 min.
Remove from the heat and add the lentils, soy sauce, balsamic vinegar and 100ml water.
Season, then tip the mixture into a casserole dish.
Rinse the saucepan and return to the hob. Add a kettle full of boiled water and bring back to the boil over a high heat.
Add the potato slices, cook for 3 mins, then drain. Arrange on top of the lentils, then brush with the remaining oil.
Roast in the oven for 25 mins until the potatoes are golden, then scatter over the thyme before serving.
		""",
        "ingredients" : {"Onion":["1",False],"Portobello":["300g",True],"Green lentil":["240g drained",True],"Olive oil":["2 tbsp",False],"Sweet potato":["1",False],"Potato":["1",False],"Garlic":["2 cloves, crushed",True],"Soy sauce":["1 tbsp",False],},
        "category" : ["Mains", "Lunch", "Dinner",],
        "prep_time" : 10,"cook_time" : 35,"servings" : 4,"difficulty" : "medium","pub_date" : datetime(2020,2,11,14,46,45,0,tzinfo=pytz.UTC),"stars" : 85,"filename" : "spiced-mushroom-and-lentil-hotpot.jpg"},
		 
		{"name":"Braised beluga lentils","author":"sallywalker",
        "steps":"""Melt butter in olive oil over medium heat in a saucepan. Cook and stir onion, carrot, celery, and salt until vegetables are softened and onion is translucent, about 10 minutes.
Reduce heat to low and add thyme sprigs and pepper. Stir in lentils until well coated. Add chicken stock and bring to a gentle simmer.
Reduce heat to low, cover and cook, checking occasionally, until the lentils are tender and have absorbed all the liquid, about 35 minutes. Remove from heat and discard thyme stems.
Stir in champagne vinegar and parsley. Season with salt and pepper to taste.""",
        "ingredients" : {"Onion":["1/2 cup",False],"Butter":["1 tbsp",False],"Black pepper":["1 tsp",False],"Belunga lentil":["1 cup",True],"Olive oil":["1 tbsp",False],"Carrot":["1/2 cup, diced",False],"Garlic":["2 cloves, crushed",True],},
        "category" : ["Mains", "Lunch", "Dinner"],
        "prep_time" : 15,"cook_time" : 45,"servings" : 2,"difficulty" : "medium","pub_date" : datetime(2020,2,11,14,46,45,0,tzinfo=pytz.UTC),"stars" : 85,"filename" : "braised-beluga-lentils.jpg"},
		 
		{"name":"Black beans and avocado on toast","author":"joebloggs",
        "steps":"""Mix the tomatoes, ¼ onion, lime juice and 1 tbsp oil and set aside.
Fry the remaining onion in 2 tbsp oil until it starts to soften.
Add the garlic, fry for 1 min, then add the cumin and chipotle and stir until fragrant.
Tip in the beans and a splash of water, stir and cook gently until heated through.
Stir in most of the tomato mixture and cook for 1 min, season well and add most of the coriander.
Toast the bread and drizzle with the remaining 1 tbsp oil.
Put a slice on each plate and pile some beans on top.
Arrange some slices of avocado on top, then sprinkle with the remaining tomato mixture and coriander leaves to serve.""",
        "ingredients" : {"Onion":["1",False],"Black bean":["2 cans, drained",True],"Black pepper":["1 tsp",False],"Cherry tomato":["270g",True],"Olive oil":["4 tbsp",False],"Garlic":["2 cloves, crushed",True],"Sliced bread":["2",False],},
        "category" : ["Breakfast", "Lunch", "Snacks"],
        "prep_time" : 20,"cook_time" : 10,"servings" : 2,"difficulty" : "easy","pub_date" : datetime(2021,3,4,9,46,45,0,tzinfo=pytz.UTC),"stars" : 235,"filename" : "blacked-beans-and-avocado-on-toast.jpg"},
		
		
		{"name":"Chocolate chip cookies","author":"joebloggs",
        "steps":"""Heat oven to 180C/160C fan/gas 4 and line two baking sheets with parchment.
Cream the butter and sugars together until very light and fluffy, then beat in the egg and vanilla.
Once combined, stir in the flour, bicarb, chocolate and ¼ tsp salt.
Scoop 10 large tbsps of the mixture onto the trays, leaving enough space between each to allow for spreading.
Bake for 10-12 mins or until firm at the edges but still soft in the middle – they will harden a little as they cool.
Leave to cool on the tray for a few mins before eating warm, or transfer to a wire rack to cool completely. Will keep for three days in an airtight container.""",
        "ingredients" : {"Butter":["120g",False],"Sugar":["150g",False],"Egg":["1",False],"Flour":["180g",False],"Baking powder":["1/2 tsp",False],"Dark chocolate":["150g",False],},
        "category" : ["Kid-friendly", "Snacks", "Desserts"],
        "prep_time" : 20,"cook_time" : 15,"servings" : 10,"difficulty" : "easy","pub_date" : datetime(2022,3,4,9,46,45,0,tzinfo=pytz.UTC),"stars" : 905,"filename" : "chocolate-chip-cookies.jpg"},
		 
		{"name":"Millionaires shortbread","author":"johndoe",
        "steps":"""Heat the oven to 180C/160C fan/gas 4. Lightly grease and line a 20-22cm square or rectangular baking tin with a lip of at least 3cm.
To make the shortbread, mix 250g plain flour and 75g caster sugar in a bowl. Rub in 175g softened butter until the mixture resembles fine breadcrumbs.
Knead the mixture together until it forms a dough, then press into the base of the prepared tin.
Prick the shortbread lightly with a fork and bake for 20 minutes or until firm to the touch and very lightly browned. Leave to cool in the tin.
To make the caramel, place 100g butter or margarine, 100g light muscovado sugar and the can of condensed milk in a pan and heat gently until the sugar has dissolved.
Continually stir with a spatula to make sure no sugar sticks to the bottom of the pan. (This can leave brown specks in the caramel but won’t affect the flavour.)
Turn up the heat to medium high, stirring all the time, and bring to the boil, then lower the heat back to low and stirring continuously, for about 5-10 minutes or until the mixture has thickened slightly. Pour over the shortbread and leave to cool.
For the topping, melt 200g plain or milk chocolate slowly in a bowl over a pan of hot water. Pour over the cold caramel and leave to set. Cut into squares or bars with a hot knife.""",
        "ingredients" : {"Butter":["275g",False],"Sugar":["175g",False],"Flour":["250g",False],"Milk chocolate":["150g",False],},
        "category" : ["Kid-friendly", "Snacks","Desserts"],
        "prep_time" : 25,"cook_time" : 35,"servings" : 2,"difficulty" : "easy","pub_date" : datetime(2021,3,4,9,46,45,0,tzinfo=pytz.UTC),"stars" : 235,"filename" : "millionaires-shortbread.jpg"},
		
		{"name":"Naughty chocolate fudge cake","author":"sallywalker",
        "steps":"""Heat the oven to 180C/160C fan/gas 4. Oil and line the base of two 18cm sandwich tins. Sieve the flour, cocoa powder and bicarbonate of soda into a bowl. Add the caster sugar and mix well.
Make a well in the centre and add the golden syrup, eggs, sunflower oil and milk. Beat well with an electric whisk until smooth.
Pour the mixture into the two tins and bake for 25-30 mins until risen and firm to the touch. Remove from oven, leave to cool for 10 mins before turning out onto a cooling rack.
To make the icing, beat the unsalted butter in a bowl until soft. Gradually sieve and beat in the icing sugar and cocoa powder, then add enough of the milk to make the icing fluffy and spreadable.
Sandwich the two cakes together with the butter icing and cover the sides and the top of the cake with more icing.""",
        "ingredients" : {"Butter":["100g",False],"Skim milk":["150ml",False],"Sugar":["150g",False],"Egg":["2",True],"Flour":["250g",False],"Dark chocolate":["150g",False],"Baking powder":["1 tsp",False],},
        "category" : ["Kid-friendly", "Desserts"],
        "prep_time" : 25,"cook_time" : 30,"servings" : 8,"difficulty" : "easy","pub_date" : datetime(2022,1,5,16,31,45,0,tzinfo=pytz.UTC),"stars" : 25,"filename" : "naughty-chocolate-fudge-cake.jpg"},
		
		{"name":"Classic fruit salad","author":"johndoe",
        "steps":"""Wash and peel all the fruit (as appropriate).
Slice all the fruit into bite-sized pieces and place in a large mixing bowl.
Drizzle the honey on top of the fruit salad, gently toss everything together, and enjoy!""",
        "ingredients" : {"Strawberry":["1 lb",True],"Banana":["5",True],"Blueberry":["2 cups",True],"Raspberry":["2 cups",True],"Mandarin":["3",True],"Honey":["2tbsp",False],},
        "category" : ["Kid-friendly", "Desserts","Breakfast","Healthy","Vegan"],
        "prep_time" : 20,"cook_time" : 20,"servings" : 10,"difficulty" : "easy","pub_date" : datetime(2022,1,6,18,51,45,0,tzinfo=pytz.UTC),"stars" : 535,"filename" : "classic-fruit-salad.jpg"},
		
		{"name":"Carajillo","author":"johndoe",
        "steps":"""Pour an espresso shot.
While it's still hot, add the brandy and mix.
Layer the cream on top of the mix.
Enjoy!""",
        "ingredients" : {"Espresso":["1 shot",False],"Brandy":["1/4 cup",False],"Cream":["1/4 cup",False],},
        "category" : ["Desserts","Breakfast"],
        "prep_time" : 5,"cook_time" : 10,"servings" : 1,"difficulty" : "easy","pub_date" : datetime(2022,1,6,18,51,45,0,tzinfo=pytz.UTC),"stars" : 535,"filename" : "carajillo.jpg"},
		
		
		{"name":"Ratatouille","author":"sallywalker",
        "steps":"""Cut 2 large aubergines in half lengthways. Place them on the board, cut side down, slice in half lengthways again and then across into 1.5cm chunks.
Peel 2 red or yellow peppers from stalk to bottom. Hold upright, cut around the stalk, then cut into 3 pieces.
Cut away any membrane, then chop into bite-size chunks.
Score a small cross on the base of each of 4 large ripe tomatoes, then put them into a heatproof bowl. Pour boiling water over, leave for 20 secs, then remove.
Pour the water away, replace the tomatoes and cover with cold water. Leave to cool, then peel the skin away.
Quarter the tomatoes, scrape away the seeds with a spoon, then roughly chop the flesh.
Set a sauté pan over medium heat and when hot, pour in 2 tbsp olive oil. Brown the aubergines for 5 mins on each side until the pieces are soft. Set them aside.
Fry the courgettes in another tbsp oil for 5 mins, until golden on both sides. Repeat with the peppers. Don’t overcook the vegetables at this stage.
Tear up the leaves from the bunch of basil and set aside. Cook 1 thinly sliced medium onion in the pan for 5 minutes. Add 3 crushed garlic cloves and fry for a further minute. Stir in 1 tbsp red wine vinegar and 1 tsp sugar, then tip in the tomatoes and half the basil.
Return the vegetables to the pan with some salt and pepper and cook for 5 mins. Serve with basil.""",
        "ingredients" : {"Aubergine":["2",True],"Yellow pepper":["2",True],"Tomato":["4",True],"Olive oil":["5 tbsp",False],"Onion":["1",False],"Garlic":["3 cloves",True],"Red wine":["1 tbsp",False],},
        "category" : ["Mains", "Lunch", "Dinner","Vegan", "Healthy","Vegetarian"],
        "prep_time" : 15,"cook_time" : 35,"servings" : 10,"difficulty" : "medium","pub_date" : datetime(2022,1,6,18,51,45,0,tzinfo=pytz.UTC),"stars" : 76,"filename" : "ratatouille.jpg"},
        
		
		{"name":"Cacio e pepe","author":"sallywalker",
        "steps":"""Cook the pasta for 2 mins less than pack instructions state, in salted boiling water.
Meanwhile, melt the butter in a medium frying pan over a low heat, then add the ground black pepper and toast for a few minutes.
Drain the pasta, keeping 200ml of the pasta water. Tip the pasta and 100ml of the pasta water into the pan with the butter and pepper.
Toss briefly, then scatter over the parmesan evenly, but don’t stir – wait for the cheese to melt for 30 seconds, then once melted, toss everything well, and stir together. This prevents the cheese from clumping or going stringy and makes a smooth, shiny sauce.
Add a splash more pasta water if you need to, to loosen the sauce and coat the pasta.
Serve immediately with a good grating of black pepper.""",
        "ingredients" : {"Spaghetti":["200g",False],"Butter":["25g",False],"Black pepper":["1 tbs",False],"Parmesan":["50g",False],},
        "category" : ["Mains", "Lunch", "Dinner","Vegetarian","Under 30'"],
        "prep_time" : 5,"cook_time" : 10,"servings" : 2,"difficulty" : "easy","pub_date" : datetime(2020,1,7,18,51,45,0,tzinfo=pytz.UTC),"stars" : 91,"filename" : "cacio-e-pepe.png"},
       
        {"name":"Coconut oil apple crisp","author":"johndoe",
        "steps":"""Preheat the oven to 350 degrees. Grease a 9×13 baking dish. Toss the apples with the almond meal and cinnamon and spread in a single layer in the baking dish.
Whisk the coconut oil and honey together until smooth. Place the rolled oats, pecans, almond meal, cinnamon, and salt in a large bowl. Add the coconut oil and honey mixture; stir until combined.
Pour the oat mixture over the apples to cover them evenly. Bake for 30-40 minutes until the topping is browning slightly. Let stand for 15-20 minutes.""",
        "ingredients" : {"Red apple":["4",True],"Cinnamon":["2 tsp",False],"Coconut oil":["1 cup",False],"Honey":["1/2 cup",False],"Pecan":["1/2 cup",True],"Salt":["1/2 tsp",False],},
        "category" : ["Healthy","Desserts","Breakfast","Vegetarian","Under 30'"],
        "prep_time" : 5,"cook_time" : 40,"servings" : 10,"difficulty" : "medium","pub_date" : datetime(2020,1,7,18,51,45,0,tzinfo=pytz.UTC),"stars" : 91,"filename" : "coconut-oil-apple-crisp.jpg"},
		
		{"name":"Blueberry scones","author":"joebloggs",
        "steps":"""Preheat oven to 400 degrees F (204 degrees C) and line a baking sheet with parchment paper (or leave bare).
Combine spelt flour, all purpose flour, baking powder, organic cane sugar, salt, and rosemary. Whisk to combine.
Add room temperature coconut oil and use a pastry cutter (or fork) to cut it into the mixture until only small bits remain.
Gently transfer to a floured surface and use your hands to form it into a disc about 1 inch in height. Use a large knife to cut the circle into 6 even wedges (or 8 for smaller scones // amount as original recipe is written // adjust if altering batch size). Then use a floured spatula to transfer the scones to the prepared baking sheet. Sprinkle the tops with a bit more cane sugar.
Bake for 22-27 min or until fluffy and light golden brown on the edges. Let cool slightly before enjoying.
Best when fresh. Once completely cooled, store leftovers at room temperature in a well-sealed container for up to 3 days. Freeze for longer term storage. These are delicious plain, but they would also be delicious heated with a bit of vegan butter.""",
        "ingredients" : {"Almond milk":["3/4 cup",False],"Egg":["1",False],"Flour":["3/4 cup",False],"Coconut oil":["6 tbsp",False],"Blueberry":["1/3 cup, frozen",True],"Rosemary":["1 tbsp",False],"Salt":["1/2 tsp",False],"Brown sugar":["1/4 cup",False],"Baking powder":["1 tbsp",False],},
        "category" : ["Healthy","Desserts","Breakfast",],
        "prep_time" : 5,"cook_time" : 25,"servings" : 8,"difficulty" : "medium","pub_date" : datetime(2015,10,7,18,51,45,0,tzinfo=pytz.UTC),"stars" : 39,"filename" : "blueberry-scones.png"},
		 
		
		{"name":"Garlic hemp oil salad dressing","author":"johndoe",
        "steps":"""Whisk all ingredients together until fully incorporated.
Let sit for an hour so the flavor of the garlic comes through.
Shake well and drizzle onto a salad.""",
        "ingredients" : {"Hemp seed oil":["1/4 cup",False],"Garlic":["4 cloves",True],"Black pepper":["1/8 tsp",False],},
        "category" : ["Vegan","Lunch","Dinner"],
        "prep_time" : 5,"cook_time" : 65,"servings" : 10,"difficulty" : "easy","pub_date" : datetime(2018,11,7,18,51,45,0,tzinfo=pytz.UTC),"stars" : 65,"filename" : "garlic-hemp-oil-salad-dressing.jpg"}

         ]

def get_all_recipes():
    return recipes
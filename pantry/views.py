from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pantry.models import Recipe, Category, Ingredient, IngredientList, UserProfile
from pantry.forms import UserForm, UserProfileForm, EmailForm, RecipeForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse

#Starring Functionality
@login_required
def star(request, recipe_name_slug, username):
    recipe_name_slug = recipe_name_slug.capitalize()
    r = Recipe.objects.get(title=recipe_name_slug)
    r.stars += 1
    r.save()

    u = UserProfile.objects.get(user=User.objects.get(username=username))
    u.starred.add(r)
    u.save()

    data = {"name" : "calum"}


    return JsonResponse('data', safe=False)

#Unstarring Functionality
@login_required
def unstar(request, recipe_name_slug, username):
    recipe_name_slug = recipe_name_slug.capitalize()
    r = Recipe.objects.get(title=recipe_name_slug)
    r.stars -= 1
    r.save()

    u = UserProfile.objects.get(user=User.objects.get(username=username))
    u.starred.remove(r)
    u.save()

    data = {"name" : "calum"}


    return JsonResponse('data', safe=False)

# Helper method for sorted recipe display
def sort_by(recipes, sort, by_ingredient=False):    
    if sort == "newest":
        recipes_sorted = sorted(recipes, key=lambda x: x.pub_date, reverse=True)
        sort_type = "Newest"
    elif sort == "oldest":
        recipes_sorted = sorted(recipes, key=lambda x: x.pub_date)
        sort_type = "Oldest"
    elif (sort == "popular") or (not by_ingredient):
        recipes_sorted = sorted(recipes, key=lambda x: x.stars, reverse=True)
        sort_type = "Most Popular"
    else:
        recipes_sorted = sorted(list(recipes.keys()), key=lambda x: recipes[x], reverse=True)
        sort_type = "Best Match"
    return recipes_sorted, sort_type

# Helper method for switching sorting type or redirecting invalid sorting types
def sort_redirect(sort, sort_new, link, param=None, by_ingredient=False):
    sort_types = {"popular", "newest", "oldest"}
    args = [param] if param else []
    # Special situation: search by ingredient, where best match sort also allowed
    special = by_ingredient and sort == "best_match"
    special_new = by_ingredient and sort_new == "best_match"

    # New sort type has been appended to the url
    if sort_new:
        # If valid redirect to it
        if (sort_new in sort_types) or special_new:
            args.append(sort_new)
            return True, redirect(reverse('pantry:' + link, args=tuple(args)))
        # If invalid discard it
        elif (sort in sort_types) or special:
            args.append(sort)
            return True, redirect(reverse('pantry:' + link, args=tuple(args)))

    # If first sort type is invalid discard it too
    if (sort not in sort_types) and not special:
        return True, redirect(reverse('pantry:' + link, args=tuple(args)))
    return False, None
    
# Helper method for ingredient display
def all_ingredients():
    types = Ingredient.get_types()
    type_names = []
    ingredients = {}
    
    for t in types:
        i = Ingredient.objects.filter(ingredient_type=t[0])
        if i.count() > 0:
            type_names.append(t[1])
            ingredients[t[1]] = i
            
    return type_names, ingredients

# Dummy
@login_required
def edit_profile(request, username):
    return HttpResponse("Edit profile")

# Renders the user profile page and passes a context dictionary with the recipes starred and written by the user
#NOTE: Not fully tested as you cannot currently create recipes
@login_required
def user_profile(request, username):
    # Renders the user profile page and passes a context dictionary with the recipes starred and written by the user
    context_dict = {"user_accessed": None, "user_profile": None, "profile_picture": None}
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        context_dict["user_accessed"] = user
        context_dict["user_profile"] = user_profile
        written_recipes = Recipe.objects.filter(author=user).order_by('-pub_date')
        context_dict["written_recipes"] = written_recipes[:4]
        context_dict["written_count"] = written_recipes.count()
        starred_recipes = user_profile.starred.all().order_by('-pub_date')
        context_dict["starred_recipes"] = starred_recipes[:4]
        context_dict["starred_count"] = starred_recipes.count()
        context_dict["profile_picture"] = user_profile.profile_picture
    except Exception as e:
        print(e)
        
    return render(request, 'pantry/user_profile.html', context=context_dict)
    
#Filters recipes by author, making sure they were written by the currently signed in user (includes sorting function).
#NOTE: Not fully tested as you cannot currently create recipes
@login_required
def show_my_recipes(request, username, sort=None, sort_new=None):
    # Handle changes in sorting type and invalid sort types
    if sort:
        invalid, redir = sort_redirect(sort, sort_new, "my_recipes", username)
        if invalid:
            return redir
    
    context_dict = {"user_accessed": None}
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        recipes = Recipe.objects.filter(author=user)
        recipes, sort_type = sort_by(list(recipes), sort)
        
        context_dict["user_accessed"] = user
        context_dict["recipes"] = recipes
        context_dict["sort_type"] = sort_type
    except Exception as e:
        print(e)
    return render(request, 'pantry/show_my_recipes.html', context=context_dict)
 

#Filters the recipes by those starred by the user (includes sorting function).
#NOTE: Not fully tested as you cannot currently create recipes 
@login_required
def show_starred_recipes(request, username, sort=None, sort_new=None):
    # Handle changes in sorting type and invalid sort types
    if sort:
        invalid, redir = sort_redirect(sort, sort_new, "starred_recipes", username)
        if invalid:
            return redir

    context_dict = {"user_accessed": None}
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        recipes = user_profile.starred.all()
        recipes, sort_type = sort_by(list(recipes), sort)
        
        context_dict["user_accessed"] = user
        context_dict["recipes"] = recipes
        context_dict["sort_type"] = sort_type
    except Exception as e:
        print(e)
    return render(request, 'pantry/show_starred_recipes.html', context=context_dict)
    
def home(request):
    # Renders the home page, passing a context dictionary with the 2 most popular and 2 most viewed recipes.
    context_dict = {}
    context_dict["popular_list"] = Recipe.objects.order_by("-stars")[:2]
    context_dict["recent_list"] = Recipe.objects.order_by("-pub_date")[:2]
    return render(request, 'pantry/home.html', context_dict)
    
def show_recipe(request, recipe_name_slug):
    try:
        context_dict = {}
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        context_dict["recipe"] = recipe
        context_dict["method"] = recipe.steps.split("/n")
        context_dict["ingredients"] = IngredientList.objects.filter(recipe=recipe)
        context_dict["categories"] = recipe.category.all()
        return render(request, 'pantry/show_recipe.html', context=context_dict)
    except Recipe.DoesNotExist:
        return render(request, 'pantry/show_recipe.html', {})
    
@login_required
def add_recipe_ingredients(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
    
        if form.is_valid():
            form.save(commit=True)
            return redirect('/pantry/add_recipe/method')
        else:
            print(form.errors)
            return render(request, 'pantry/add_recipe.html', {'form': form})
    else:
        type_names, ingredients = all_ingredients()
        context_dict = {"types": type_names, "ingredients": ingredients}
        return render(request, 'pantry/add_recipe_ingredients.html', context=context_dict)

@login_required
def add_recipe_method(request):
    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('/pantry/')
        else:
            print(form.errors)
    return render(request, 'pantry/add_recipe_method.html', {'form': form})

def show_category(request, category_title_slug, sort=None, sort_new=None):
    # Handle changes in sorting type and invalid sort types
    if sort:
        invalid, redir = sort_redirect(sort, sort_new, "show_category", category_title_slug)
        if invalid:
            return redir
    
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_title_slug)
        recipes = Recipe.objects.filter(category=category)
        recipes, sort_type = sort_by(list(recipes), sort)

        context_dict['recipes'] = recipes
        context_dict['category'] = category
        context_dict['sort_type'] = sort_type
    except Category.DoesNotExist:
        context_dict["false_category"] = category_title_slug
        return render(request, 'pantry/show_category.html', context=context_dict)
        
    return render(request, 'pantry/show_category.html', context=context_dict)


def search_by_ingredient(request):
    type_names, ingredients = all_ingredients()
    context_dict = {"types": type_names, "ingredients": ingredients}
    return render(request, 'pantry/search_by_ingredient.html', context=context_dict)


def search_by_ingredient_results(request, sort=None, sort_new=None):
    # Handle changes in sorting type and invalid sort types
    if sort:
        invalid, redir = sort_redirect(sort, sort_new, "search_by_ingredient_results", by_ingredient=True)
        if invalid:
            return redir
    
    if request.method == 'POST':
        ingredients = request.POST.getlist('ingredients')
    else:
        ingredients = request.session.get('ingredients')

    recipe_percents = {}
    if ingredients:
        print(ingredients)
        for name in ingredients:
            ingredient = Ingredient.objects.get(name=name)
            recipes = IngredientList.objects.filter(ingredient=ingredient).values('recipe')
            recipes = {Recipe.objects.get(pk=r['recipe']) for r in recipes}
            
            # Keeping count of how many selected ingredients each recipe has
            for recipe in recipes:
                if recipe not in recipe_percents:
                    recipe_percents[recipe] = 1
                else:
                    recipe_percents[recipe] += 1

        # Mapping to each recipe the percentage of its total ingredients that the user has selected
        for recipe, selected in recipe_percents.items():
            total = recipe.ingredients.count()
            recipe_percents[recipe] = int(100 * selected / total);
            
        recipes, sort_type = sort_by(recipe_percents, sort, True)
        request.session['ingredients'] = ingredients
        context_dict = {"recipes" : recipes, "recipe_percents": recipe_percents, "sort_type" : sort_type, "done": True}
        return render(request, 'pantry/search_by_ingredient_results.html', context=context_dict)
    else:
        return redirect(reverse('pantry:search_by_ingredient'))


def search_results(request, sort=None, sort_new=None):
    # Handle changes in sorting type and invalid sort types
    if sort:
        invalid, redir = sort_redirect(sort, sort_new, "search_results")
        if invalid:
            return redir

    if request.method == 'POST':
        searched = request.POST.get('searched')
    else:
        searched = request.session.get('searched')
        
    recipes = set()
    if searched:
        keywords = searched.split()
        for k in keywords:
            recipes = recipes.union(Recipe.objects.filter(Q(title__contains=k) | Q(steps__contains=k)))
            for cat in Category.objects.filter(Q(name__contains=k)):
                recipes = recipes.union(cat.recipe_set.all())
            
        recipes, sort_type = sort_by(list(recipes), sort)
        request.session['searched'] = searched
        context_dict = {'searched': searched, 'recipes':recipes, 'sort_type': sort_type}
        return render(request, 'pantry/search_results.html', context=context_dict)
    else: 
        return render(request, 'pantry/search_results.html', {})

# Register view
def sign_up(request):
    registered = False
    email = request.session.get('email')
    if email:
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.email = email
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                registered = True
                
                user = authenticate(username=user_form.data["username"], password=user_form.data["password"])
                login(request, user)
            else:
                context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'error': list(user_form.errors.values())[0]}
                return render(request, 'pantry/sign_up.html', context=context_dict)
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()
        
        context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
        return render(request, 'pantry/sign_up.html', context=context_dict)
    else:
        return redirect(reverse('pantry:check_email'))

# Check email view before logging in / signing up
def check_email(request):
    # If HTTP POST we want to process data
    if request.method == 'POST':
        # Gather email provided by the user
        email_form = EmailForm(request.POST)
        
        if email_form.is_valid():
            user_email = email_form.data["email"]
            
            # If email exists, should redirect to sign in page
            if User.objects.filter(email=user_email).exists():
                user = User.objects.get(email=user_email)
                request.session['username'] = user.username
                return render(request, 'pantry/sign_in.html', context = {'username': user.username})
            else:
                # If email does not exist redirect to signup page
                request.session['email'] = user_email
                user_form = UserForm()
                profile_form = UserProfileForm()
                return render(request, 'pantry/sign_up.html', {'user_form': user_form, 'profile_form': profile_form})
        else:
            context_dict = {'email_form': email_form, 'error': list(email_form.errors.values())[0]}
            return render(request, 'pantry/check_email.html', context=context_dict)
    # No context variables to pass to template system, redirect to signup page
    else:
        email_form = EmailForm()
        
    return render(request, 'pantry/check_email.html', context = {'email_form': email_form})

# Sign in view
def sign_in(request):
    username = request.session.get('username')
    if username:
        if request.method == 'POST':
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            context_dict = {'username':username}
        
            if user:
                if user.is_active:
                    login(request, user)
                    context_dict['success'] = "You've signed in successfully!"
                else:
                    context_dict['error'] = "Your Pantry account is disabled."
            else:
                print(f"Invalid login details: {request.session['username']}, {password}")
                context_dict['error'] = "Wrong password, try again."
            
            return render(request, 'pantry/sign_in.html', context=context_dict)

        else:
            return redirect(reverse('pantry:check_email'))
    else:
        return redirect(reverse('pantry:check_email'))

# Logout view restricted to authenticated users
@login_required
def sign_out(request):
    logout(request)
    return redirect(reverse('pantry:home'))

def pagenotfound(request, exception):
    return render(request, "errors/404.html", {})
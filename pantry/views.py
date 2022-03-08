from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pantry.models import Recipe, Category, Ingredient, IngredientList, UserProfile
from pantry.forms import UserForm, UserProfileForm, EmailForm, RecipeForm
from django.contrib.auth.models import User
from django.db.models import Q

# Helper method for sorted recipe display
def sort_by(recipes, sort):
    if sort == "newest":
        recipes.sort(key=lambda x: x.pub_date, reverse=True)
        sort_type = "Newest"
    elif sort == "oldest":
        recipes.sort(key=lambda x: x.pub_date)
        sort_type = "Oldest"
    else:
        recipes.sort(key=lambda x: x.stars, reverse=True)
        sort_type = "Most Popular"
    return recipes, sort_type


# Dummy views until created
    
def edit_profile(request, username):
    return HttpResponse("Edit profile")


# DONE
@login_required
def user_profile(request, username):
    # Renders the user profile page and passes a context dictionary with the recipes starred and written by the user
    context_dict = {"user_accessed": None, "user_profile": None, "profile_picture": None}
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        context_dict["user_accessed"] = user
        context_dict["user_profile"] = user_profile
        context_dict["written_recipes"] = Recipe.objects.filter(author=user)
        context_dict["written_count"] = context_dict["written_recipes"].count()
        context_dict["starred_recipes"] = user_profile.starred.all()
        context_dict["starred_count"] = context_dict["starred_recipes"].count()
        context_dict["profile_picture"] = user_profile.profile_picture
    except Exception as e:
        print(e)
        
    return render(request, 'pantry/user_profile.html', context=context_dict)
    
def show_my_recipes(request, username, sort=None):
    context_dict = {"user_accessed": None}
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        recipes = Recipe.objects.filter(author=user)
        recipes, sort_type = sort_by(list(recipes), sort)
        
        context_dict["user_accessed"] = user
        context_dict["recipes"] = recipes
    except Exception as e:
        print(e)
    return render(request, 'pantry/show_my_recipes.html', context=context_dict)
    
def show_starred_recipes(request, username, sort=None):
    context_dict = {"user_accessed": None}
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        recipes = user_profile.starred.all()
        recipes, sort_type = sort_by(list(recipes), sort)
        
        context_dict["user_accessed"] = user
        context_dict["recipes"] = recipes
    except Exception as e:
        print(e)
    return render(request, 'pantry/show_starred_recipes.html', context=context_dict)
    
def search_by_ingredient(request):
    context_dict = {}
    types = Ingredient.get_types()
    type_names = []
    ingredients = {}
    
    for t in types:
        i = Ingredient.objects.filter(ingredient_type=t[0])
        if i.count() > 0:
            type_names.append(t[1])
            ingredients[t[1]] = i
    
    context_dict["types"] = type_names    
    context_dict["ingredients"] = ingredients
    return render(request, 'pantry/search_by_ingredient.html', context=context_dict)
    
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
        context_dict["ingredients"] = IngredientList.objects.filter(recipe=recipe)
        return render(request, 'pantry/show_recipe.html', context=context_dict)
    except Recipe.DoesNotExist:
        return render(request, 'pantry/show_recipe.html', {})
    
@login_required
def add_recipe_ingredients(request):
	form = RecipeForm()
	
	ingredients = Ingredient.objects.filter
	
	if request.method == 'POST':
		form = RecipeForm(request.POST)
	
		if form.is_valid():
			form.save(commit=True)
			return redirect('/pantry/add_recipe/method')
		else:
			print(form.errors)
	return render(request, 'pantry/add_recipe.html', {'form': form})

@login_required
def add_recipe_method(request):
	form = RecipeMethodForm()
	
	if request.method == 'POST':
		form = RecipeMethodForm(request.POST)
		
		if form.is_valid():
			form.save(commit=True)
			return redirect('/pantry/')
		else:
			print(form.errors)
	return render(request, 'pantry/add_recipe_method.html', {'form': form})

def show_category(request, category_title_slug, sort=None):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_title_slug)
        recipes = Recipe.objects.filter(category=category)
        recipes, sort_type = sort_by(list(recipes), sort)

        context_dict['recipes'] = recipes
        context_dict['category'] = category
        context_dict['sort_type'] = sort_type
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None
    return render(request, 'pantry/show_category.html', context=context_dict)


def keyword_search_results(request, sort=None):
    if request.method == 'POST':
        searched = request.POST.get('searched')
    else:
        searched = request.session['searched']
        
    recipes = set()
    if searched:
        keywords = searched.split()
        for k in keywords:
            recipes = recipes.union(Recipe.objects.filter(Q(title__contains=k) | Q(steps__contains=k)))
            
        recipes, sort_type = sort_by(list(recipes), sort)
        request.session['searched'] = searched
        context_dict = {'searched': searched, 'recipes':recipes, 'sort_type': sort_type}
        return render(request, 'pantry/search_results.html', context=context_dict)
    else: 
        return render(request, 'pantry/search_results.html', {})


# Register view
def sign_up(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.email = request.session['email']
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
    if request.method == 'POST':
        username = request.session['username']
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


# Logout view restricted to authenticated users
@login_required
def sign_out(request):
    logout(request)
    return redirect(reverse('pantry:home'))
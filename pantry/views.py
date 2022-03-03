from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from pantry.models import Recipe, Category, Ingredient, IngredientList, UserProfile
from pantry.forms import UserForm, UserProfileForm, EmailForm, RecipeIngredientsForm
from django.contrib.auth.models import User
from django.db.models import Q

# Dummy views until created
def show_my_recipes(request, username):
    return HttpResponse("My recipes")
    
def show_starred_recipes(request, username):
    return HttpResponse("Starred recipes")
    
def search_by_ingredient(request):
    return HttpResponse("Search by ingredient")

@login_required
def user_profile(request, username):
    # Renders the user profile page and passes a context dictionary with the recipes starred and written by the user
    context_dict = {}
    context_dict["written_list"] = Recipe.objects.filter(author= username) #Not sure if username is the user object or just the name
    return render(request, 'pantry/user_profile.html', context=context_dict)
    
    
    
def home(request):
    # Renders the home page, passing a context dictionary with the 6 most popular and 6 most viewed recipes.
    context_dict = {}
    context_dict["popular_list"] = Recipe.objects.order_by("-stars")[:6]
    context_dict["recent_list"] = Recipe.objects.order_by("-pub_date")[:6]
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
	form = RecipeIngredientsForm()
	
	if request.method == 'POST':
		form = RecipeIngredientsForm(request.POST)
	
		if form.is_valid():
			form.save(commit=True)
			return redirect('/pantry/add_recipe/method')
		else:
			print(form.errors)
	return render(request, 'pantry/add_recipe_ingredients.html', {'form': form})

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



def show_category(request, category_title_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_title_slug)
        recipes = Recipe.objects.filter(category=category)
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None
    return render(request, 'pantry/show_category.html', context=context_dict)


def keyword_search_results(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        recipes = set()
        if searched:
            keywords = searched.split()
            for k in keywords:
                recipes = recipes.union(Recipe.objects.filter(Q(title__contains=k) | Q(steps__contains=k)))
            context_dict = {'searched':searched, 'recipes':recipes}
            return render(request, 'pantry/search_results.html', context=context_dict)
        else: 
            return render(request, 'pantry/search_results.html', {})
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


# Logout view restricted to authenticated users
@login_required
def sign_out(request):
    logout(request)
    return redirect(reverse('pantry:home'))

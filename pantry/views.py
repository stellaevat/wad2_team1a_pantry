from django.shortcuts import render
<<<<<<< HEAD
from pantry.forms import UserForm, UserProfileForm, recipeForm
=======
>>>>>>> cfd375a2b11844700b0545720943db5212a02577
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from pantry.models import Category

from pantry.models import Recipe, Category, Ingredient, UserProfile
from pantry.forms import UserForm, UserProfileForm, EmailForm

# Dummy views until created
def home(request):
    return render(request, 'pantry/home.html', {})
    
def show_recipe(request):
	context_dict = {}
	recipe = Recipe.objects.get(slug=recipe_name_slug)
    return HttpResponse("Show recipe")
    
def show_category(request):
    context_dict = {}
	try:
		category = Category.objects.get(slug=category_title_slug)
		recipes = Recipe.objects.filter(category=category)
		context_dict['recipes'] = recipes
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['recipes'] = None
	return render(request, 'pantry/category.html', context=context_dict)


def show_recipe(request, recipe_name_slug):
    return HttpResponse("Show recipe")
    
def show_category(request, category_title_slug):
    return HttpResponse("Show category")
    
def search_by_ingredient(request):
    return HttpResponse("Search by ingredient")
  
@login_required
def add_recipe(request):
	form = recipeForm()
	
	if request.method == 'POST':
		form = recipeForm(request.POST)
	
		if form.is_valid():
			form.save(commit=True)
			return redirect('/pantry/')
		else:
			print(form.errors)
	return render(request, 'pantry/add_recipe.html', {'form': form})

    
def user_profile(request):
    return HttpResponse("User profile")


# Search by keyword results
def keyword_search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(title__contains=searched)
        context_dict = {'searched':searched, 'recipes':recipes}
        return render(request, 'pantry/search_results.html', context=context_dict)
    else:
        return render(request, 'pantry/search_results.html', {})

# Register view
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        
    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'pantry/register.html', context=context_dict)

# Check email view before logging in / signing up
def check_email(request):
    # If HTTP POST we want to process data
    if request.method == 'POST':
        # Gather email provided by the user
        user_email = request.POST.get('email')
        email_form = EmailForm(request.POST)

        # Check if email is valid address
        try:
            validate_email(user_email)
        except ValidationError as e:
            print("The email is invalid.")

        # If email exists, should redirect to login page
        if User.objects.filter(email=user_email).exists():
            user = User.objects.get(email=user_email)
            return render(request, 'pantry/login.html', context = {'username': user.username})
        else:
            # If email does not exist redirect to signup page
            return render(request, 'pantry/signup.html', context = {'email': user_email})

    # No context variables to pass to template system, redirect to signup page
    else:
        email_form = EmailForm()
    
    return render(request, 'pantry/check_email.html', context = {'email': email_form})

# Login view
def user_login(request, username):
    if request.method == 'POST':
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('pantry:home'))
            else:
                return HttpResponse("Your Pantry account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'pantry/login.html', username)


# Logout view restricted to authenticated users
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('pantry:home'))

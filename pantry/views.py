import datetime
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from pantry.models import Recipe, Category, Ingredient, IngredientList, UserProfile
from pantry.forms import UserForm, UserProfileForm, EmailForm, RecipeForm, RecipeIngredientsForm, RecipeQuantitesForm, EditProfilePicture, EditUsername, EditEmail, EditPassword
from django.contrib.auth.models import User
from django.db.models import Q


#----------------------------------------------------------------------------
# HELPER METHODS
#----------------------------------------------------------------------------
# Stores any fields added to request.session to pass info from one view to the other
session_modifications = set()

# Clears added fields from request.session when no longer required
# Needs to be called at the beginning of every view
def reset_session(request, exception=None):
    removed_modifications = set()
    for mod in session_modifications:
        if request.session.get(mod):
            if not exception or mod not in exception:
                del request.session[mod]
                removed_modifications.add(mod)
    for mod in removed_modifications:
        session_modifications.remove(mod)
    return request


# Handling sorted recipe display
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


# Switching sorting type or redirecting invalid sorting types
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
    
    
# Returns available ingredients under their types
# Parameter 'used' determines whether want all or just the ones used in recipes
def all_ingredients(used=False):
    types = Ingredient.get_types()
    type_names = []
    ingredients = {}
    
    for t in types:
        ings = Ingredient.objects.filter(ingredient_type=t[0])
        if used:
            ings = [i for i in ings if IngredientList.objects.filter(ingredient=i)]
        if ings:
            type_names.append(t[1])
            ingredients[t[1]] = ings
            
    return type_names, ingredients


# Initialising the edit profile forms with user details
def edit_profile_forms(request, user_profile):
    username_form = EditUsername(instance = request.user)
    email_form = EditEmail(instance = user_profile)
    pass_form = EditPassword(request.user)
    img_form = EditProfilePicture(instance = user_profile)
    return username_form, email_form, pass_form, img_form


#----------------------------------------------------------------------------
# AJAX CALLS
#----------------------------------------------------------------------------
# Author deletes recipe
@login_required
def delete_recipe(request, recipe_name_slug, username):
    recipe_name_slug = request.GET['recipe_name_slug']
    username = request.GET['username']
    recipe = Recipe.objects.filter(slug=recipe_name_slug)
    
    if recipe:
        recipe = recipe[0]
        if recipe.picture:
                recipe.picture.delete(save = False)
        recipe.delete()

    data = {"username" : username}

    return JsonResponse('data', safe=False)


#Starring Functionality
@login_required
def star(request, recipe_name_slug, username):
    recipe_name_slug = request.GET['recipe_name_slug']
    username = request.GET['username']
    r = Recipe.objects.get(slug=recipe_name_slug)
    r.stars += 1
    r.save()

    u = UserProfile.objects.get(user=User.objects.get(username__iexact=username))
    u.starred.add(r)
    u.save()

    data = {}

    return JsonResponse('data', safe=False)

#Unstarring Functionality
@login_required
def unstar(request, recipe_name_slug, username):
    recipe_name_slug = request.GET['recipe_name_slug']
    username = request.GET['username']
    r = Recipe.objects.get(slug=recipe_name_slug)
    r.stars -= 1
    r.save()

    u = UserProfile.objects.get(user=User.objects.get(username=username))
    u.starred.remove(r)
    u.save()

    data = {}
    
    return JsonResponse('data', safe=False)
    

#----------------------------------------------------------------------------
# VIEWS AVAILABLE TO ALL USERS
#----------------------------------------------------------------------------
# Renders the home page, with 2 most popular and 2 most viewed recipes
def home(request):
    request = reset_session(request)
    
    context_dict = {}
    context_dict["popular_list"] = Recipe.objects.order_by("-stars")[:2]
    context_dict["recent_list"] = Recipe.objects.order_by("-pub_date")[:2]
    return render(request, 'pantry/home.html', context_dict)


# Renders recipe page with all relevant info
def show_recipe(request, recipe_name_slug):
    request = reset_session(request)
    
    try:
        context_dict = {}
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        context_dict["recipe"] = recipe
        context_dict["method"] = recipe.steps.splitlines()
        context_dict["ingredients"] = IngredientList.objects.filter(recipe=recipe)
        context_dict["categories"] = recipe.category.all()
        return render(request, 'pantry/show_recipe.html', context=context_dict)
    except Recipe.DoesNotExist:
        return render(request, 'pantry/show_recipe.html', {})
 
 
# Renders page for selection of ingredients to search for
def search_by_ingredient(request):
    request = reset_session(request)
    
    type_names, ingredients = all_ingredients(used=True)
    context_dict = {"types": type_names, "ingredients": ingredients}
    return render(request, 'pantry/search_by_ingredient.html', context=context_dict)


# Renders page with results from search by ingredient (sorting functionality included)
def search_by_ingredient_results(request, sort=None, sort_new=None):
    if request.META.get('HTTP_REFERER'):
        request = reset_session(request, exception={'ingredients'})
    else:
        request = reset_session(request)
        
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
        session_modifications.add('ingredients')
        context_dict = {"recipes" : recipes, "recipe_percents": recipe_percents, "sort_type" : sort_type}
        return render(request, 'pantry/search_by_ingredient_results.html', context=context_dict)
    else:
        return redirect(reverse('pantry:search_by_ingredient'))


# Renders page of search results from search bar, if any (sorting functionality included)
def search_results(request, sort=None, sort_new=None):
    if request.META.get('HTTP_REFERER'):
        request = reset_session(request, exception={'searched'})
    else:
        request = reset_session(request)
        
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
            # Ensure keyword not surrounded by letters/digits in the text
            regex = fr'(?<![a-z0-9]){k}(?![a-z0-9])'.format(k=k)
            
            # Keyword in recipe title or method
            recipes = recipes.union(Recipe.objects.filter(Q(title__iregex=regex) | Q(steps__iregex=regex)))
            
            # Keyword in recipe category tags
            for cat in Category.objects.filter(name__iregex=regex):
                recipes = recipes.union(cat.recipe_set.all())
            
            # Keyword in recipe ingredients
            for ing in Ingredient.objects.filter(name__iregex=regex):
                lists = IngredientList.objects.filter(ingredient=ing)
                for l in lists:
                    recipes.add(l.recipe)
            
        recipes, sort_type = sort_by(list(recipes), sort)
        request.session['searched'] = searched
        session_modifications.add('searched')
        context_dict = {'searched': searched, 'recipes':recipes, 'sort_type': sort_type}
        return render(request, 'pantry/search_results.html', context=context_dict)
    else: 
        return render(request, 'pantry/search_results.html', {})

# Renders page of all recipes under specified category     
def show_category(request, category_title_slug, sort=None, sort_new=None):
    request = reset_session(request)
    
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


# Renders page of all recipes written by specific author, for public view
def show_user_recipes(request, username, sort=None, sort_new=None):
    request = reset_session(request)
    
    # Handle changes in sorting type and invalid sort types
    if sort:
        invalid, redir = sort_redirect(sort, sort_new, "user_recipes", username)
        if invalid:
            return redir
            
    context_dict = {"user_accessed": None}
    try:
        user = User.objects.get(username=username)
        if user == request.user:
            return redirect(reverse('pantry:my_recipes', args=(username,)))
        
        user_profile = UserProfile.objects.get(user=user)
        recipes = Recipe.objects.filter(author=user)
        if recipes:
            recipes, sort_type = sort_by(list(recipes), sort)
            context_dict["user_accessed"] = username
            context_dict["profile_picture"] = user_profile.profile_picture
            context_dict["user_joined"] = user.date_joined
            context_dict["recipes"] = recipes
            context_dict["sort_type"] = sort_type
    except Exception as e:
        print(e)
    return render(request, 'pantry/show_user_recipes.html', context=context_dict)
    


# Checks email before signing in / signing up, to determine which is required
def check_email(request):
    request = reset_session(request)

    # If HTTP POST we want to process data
    if request.method == 'POST':
        # Gather email provided by the user
        email_form = EmailForm(request.POST)
        
        if email_form.is_valid():
            user_email = email_form.data["email"]
            
            # If email exists, should redirect to sign in page
            if UserProfile.objects.filter(email=user_email).exists():
                profile = UserProfile.objects.get(email=user_email)
                username = profile.user.username
                request.session['username'] = username
                session_modifications.add('username')
                return render(request, 'pantry/sign_in.html', context = {'username':username})
            else:
                # If email does not exist redirect to signup page
                request.session['email'] = user_email
                session_modifications.add('email')
                user_form = UserForm()
                profile_form = UserProfileForm()
                return render(request, 'pantry/sign_up.html', {'user_form': user_form, 'profile_form': profile_form})
        else:
            context_dict = {'email_form': email_form, 'error': list(email_form.errors.values())[-1]}
            return render(request, 'pantry/check_email.html', context=context_dict)
    # No context variables to pass to template system, redirect to signup page
    else:
        email_form = EmailForm()
        
    return render(request, 'pantry/check_email.html', context = {'email_form': email_form})


# Renders registration page, using previous supplied email (from check_email)
def sign_up(request):
    if request.META.get('HTTP_REFERER'):
        request = reset_session(request, exception={'email'})
    else:
        request = reset_session(request)
        
    registered = False
    email = request.session.get('email')
    if email:
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST)

            if user_form.is_valid() and profile_form.is_valid():
                try: 
                    user = user_form.save()
                    user.set_password(user.password)
                    user.save()

                    profile = profile_form.save(commit=False)
                    profile.user = user
                    profile.email = email
                    profile.save()
                    registered = True
                    
                    user = authenticate(username=user_form.data["username"], password=user_form.data["password"])
                    login(request, user)
                except Exception as e:
                    print(e)
                    if user:
                        user.delete()
                    if profile:
                        profile.delete()
            else:
                context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'error': list(user_form.errors.values())[-1]}
                return render(request, 'pantry/sign_up.html', context=context_dict)
        else:
            user_form = UserForm()
            profile_form = UserProfileForm()
        
        context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
        return render(request, 'pantry/sign_up.html', context=context_dict)
    else:
        return redirect(reverse('pantry:check_email'))


# Renders sign in page, using previous supplied email (from check_email)
def sign_in(request):
    if request.META.get('HTTP_REFERER'):
        request = reset_session(request, exception={'username'})
    else:
        request = reset_session(request)
        
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
        

# Deletes user account upon request and notifies of successful deletion
def account_deleted(request, username):
    request = reset_session(request)
    if not request.META.get('HTTP_REFERER'):
        return redirect(reverse('pantry:home'))
        
    if User.objects.filter(username=username):
        user = User.objects.get(username=username)
        
        if UserProfile.objects.filter(user=user):
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.profile_picture != 'profile-picture-default.png':
                user_profile.profile_picture.delete(save = False)
            
        user.delete()
    else:
        return redirect(request, 'errors/404.html', {})
        
    return render(request, 'pantry/account_deleted.html', {})


# Error pages
def pagenotfound(request, exception):
    request = reset_session(request)
    return render(request, "errors/404.html", {})

def errorfound(request):
    request = reset_session(request)
    return render(request, "errors/500.html", {})
    
    
#----------------------------------------------------------------------------
# VIEWS AVAILABLE TO AUTHENTICATED USERS
#----------------------------------------------------------------------------
# Renders sign out view (never visible to user)
@login_required
def sign_out(request):
    request = reset_session(request)
    logout(request)
    return redirect(reverse('pantry:home'))

  
# Renders page for registered user to add new recipe - ingredients stage
@login_required
def add_recipe_ingredients(request):
    request = reset_session(request)
    
    type_names, ingredients = all_ingredients()
    context_dict = {"types": type_names, "ingredients": ingredients}
    
    if request.method == 'POST':
        form = RecipeIngredientsForm(request.POST)
    
        if form.is_valid():
            ingredients = request.POST.getlist('ingredients')
            request.session['ingredients'] = ingredients
            session_modifications.add('ingredients')
            return redirect(reverse('pantry:add_recipe_method'))
        else:
            print(form.errors)
            context_dict['form'] = form
            return render(request, 'pantry/add_recipe_ingredients.html', context=context_dict)
    else:
        return render(request, 'pantry/add_recipe_ingredients.html', context=context_dict)


# Renders page for registered user to add new recipe - method (and remaining info) stage
@login_required
def add_recipe_method(request):
    if request.META.get('HTTP_REFERER'):
        request = reset_session(request, exception={'ingredients'})
    else:
        request = reset_session(request)
        
    context_dict = {}
    recipe_form = RecipeForm()
    quantities_form = RecipeQuantitesForm()
    ingredients = request.session.get('ingredients')

    if ingredients:
        ingredients = [Ingredient.objects.get(name=name) for name in ingredients]
    else:
        return redirect(reverse('pantry:add_recipe_ingredients'))
    
    context_dict['categories'] = True if Category.objects.all() else False
    context_dict['ingredients'] = ingredients
    context_dict['ing_count'] = len(ingredients)
    
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES)
        quantities_form = RecipeQuantitesForm(request.POST)
        
        if recipe_form.is_valid() and quantities_form.is_valid():
            try:
                recipe = recipe_form.save(commit=False)
                recipe.pub_date = datetime.datetime.now().date()
                recipe.stars = 0
                recipe.author = request.user
                recipe.save()
                # Save categories now that recipe has id
                recipe_form.save_m2m()
                recipe.ingredients.add(*ingredients)
                recipe.save()
                # Add ingredients, quantities, plurals
                for i, ing in enumerate(ingredients):
                    ingList = IngredientList.objects.get(recipe=recipe, ingredient=ing)
                    ingList.quantity = request.POST.get(ing.name + "-quantity", "")
                    ingList.plural = True if request.POST.get(ing.name + "-plural", False) else False
                    ingList.save()

                context_dict['recipe'] = recipe
                return render(request, 'pantry/add_recipe_method.html', context=context_dict)
            except Exception as e:
                print(e)
                if recipe:
                    recipe.delete()
                context_dict['error'] = True
                return render(request, 'pantry/add_recipe_method.html', context=context_dict)
                
        else:
            print(recipe_form.errors, quantities_form.errors)
            context_dict['recipe_form'] = recipe_form
            context_dict['quantities_form'] = quantities_form
        return render(request, 'pantry/add_recipe_method.html', context=context_dict)
    
    context_dict['recipe_form'] = recipe_form
    context_dict['quantities_form'] = quantities_form
    return render(request, 'pantry/add_recipe_method.html', context=context_dict)

    
# Renders the user profile page, passing recipes starred and written by the user
@login_required
def user_profile(request, username):
    request = reset_session(request)

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
    
    
# Renders page for registered user to edit their profile (username, password, email, profile picture)
@login_required
def edit_profile(request, username):  
    request = reset_session(request)
    user = request.user
    # If wrong profile trying to be accessed, redirect to correct one
    if user.username != username:
        return redirect(reverse('pantry:edit_profile', args=(user.username,)))
        
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return render(request, 'pantry/edit_profile.html', {})

    context_dict = {}
    success_msg = "Updated succesfully!"
    if request.method == 'POST':
        username_form = EditUsername(request.POST, instance=request.user)
        email_form = EditEmail(request.POST, instance=user_profile)
        pass_form = EditPassword(request.user, request.POST)
        img_form = EditProfilePicture(request.POST, instance=user_profile)
        
        if "img-submit" in request.POST:
            if img_form.is_valid(request):
                # Update picture if new one provided, delete previous one
                if 'profile_picture' in request.FILES:
                    if user_profile.profile_picture != 'profile-picture-default.png':
                        user_profile.profile_picture.delete(save = False)
                    user_profile.profile_picture = request.FILES["profile_picture"]
                
                # Clear picture if requested, return to default
                elif request.POST.get('profile_picture-clear'):
                    if user_profile.profile_picture != 'profile-picture-default.png':
                        user_profile.profile_picture.delete(save = False)
                        user_profile.profile_picture = 'profile-picture-default.png'
                
                user_profile.save()
                context_dict['img_success'] = success_msg
            else:
                context_dict['img_error'] = list(img_form.errors.values())[-1]
            
        if "username-submit" in request.POST:
            if username_form.is_valid():
                user.username = request.POST.get("username")
                user.save()
                context_dict['username_success'] = success_msg
            else:
                context_dict['username_error'] = list(username_form.errors.values())[-1]
                # Reset request.user so url dispatcher can use the correct username
                request.user = User.objects.get(username=username)
            
            
        if "email-submit" in request.POST:
            if email_form.is_valid():
                user_profile.email = request.POST.get("email")
                user_profile.save()
                context_dict['email_success'] = success_msg
            else:
                context_dict['email_error'] = list(email_form.errors.values())[-1]

        if "pass-submit" in request.POST:
            if pass_form.is_valid():
                pass_form.save()
                update_session_auth_hash(request, pass_form.user)
                context_dict['pass_success'] = success_msg
            else:
                context_dict['pass_error'] = list(pass_form.errors.values())[-1]
                
        username_form, email_form, pass_form, img_form = edit_profile_forms(request, user_profile)
    else:
        username_form, email_form, pass_form, img_form = edit_profile_forms(request, user_profile)
        context_dict = {'pass_form': pass_form, 'img_form': img_form, 'username_form': username_form,'email_form': email_form}
     
    context_dict['pass_form'] = pass_form
    context_dict['img_form'] = img_form
    context_dict['username_form'] = username_form
    context_dict['email_form'] = email_form
    return render(request, 'pantry/edit_profile.html', context=context_dict)
    
    
#Filters recipes by author, making sure they were written by the currently signed in user (includes sorting function)
@login_required
def show_my_recipes(request, username, sort=None, sort_new=None):
    request = reset_session(request)
    
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
 

#Filters the recipes by those starred by the user (includes sorting function)
@login_required
def show_starred_recipes(request, username, sort=None, sort_new=None):
    request = reset_session(request)
    
    # Handle changes in sorting type and invalid sort types
    if sort:
        invalid, redir = sort_redirect(sort, sort_new, "starred_recipes", username)
        if invalid:
            return redir

    context_dict = {"user_accessed": None}
    try:
        user = User.objects.get(username=username)
        if user != request.user:
            return redirect(reverse('pantry:starred_recipes', args=('request.user.username',)))
        
        user_profile = UserProfile.objects.get(user=user)
        recipes = user_profile.starred.all()
        recipes, sort_type = sort_by(list(recipes), sort)
        
        context_dict["user_accessed"] = user
        context_dict["recipes"] = recipes
        context_dict["sort_type"] = sort_type
    except Exception as e:
        print(e)
    return render(request, 'pantry/show_starred_recipes.html', context=context_dict)


# Renders page notifying user that their recipe was deleted succesfully
@login_required 
def recipe_deleted(request):
    request = reset_session(request)
    if not request.META.get('HTTP_REFERER'):
        return redirect(reverse('pantry:home'))
    return render(request, 'pantry/recipe_deleted.html', {})
    
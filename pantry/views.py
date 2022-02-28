from django.shortcuts import render
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Search by keyword results
def keyword_search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        recipes = Recipe.objects.filter(title__contains=searched)
        context_dict = {'searched':searched, 'recipes'=recipes}
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
            user.set_email(request.POST.get('email')) #should it be .POST or something else?
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

    return render(request, 'pantry/register.html', context = {'user_form': user_form,'profile_form': profile_form,'registered': registered})

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
            return render(request, 'pantry/login.html', context = {'email': user_email})
        else:
            # If email does not exist redirect to signup page
            return render(request, 'pantry/signup.html', context = {'email': user_email})

    # No context variables to pass to template system, redirect to signup page
    else:
        email_form = EmailForm()
    
    return render(request, 'pantry/check_email.html', context = {'email': email_form})

# Login view
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email') # should it be .POST or something else?
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('pantry:home'))
            else:
                return HttpResponse("Your Pantry account is disabled.")
        else:
            print(f"Invalid login details: {email}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'pantry/login.html')


# Logout view restricted to authenticated users
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('pantry:home'))

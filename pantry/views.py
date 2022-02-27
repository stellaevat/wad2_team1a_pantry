from django.shortcuts import render
from rango.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

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
            return render(request, 'pantry/login.html', context = {'email': email_form})
        else:
            # If email does not exist redirect to signup page
            return render(request, 'pantry/signup.html', context = {'email': email_form})

    # No context variables to pass to template system, redirect to signup page
    else:
        email_form = EmailForm()
        return render(request, 'pantry/signup.html', context = {'email': email_form})

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('pantry:index'))
            else:
                return HttpResponse("Your Pantry account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'pantry/login.html')

# Restricted view for authenticated users
@login_required
def restricted(request):
    return render(request, 'pantry/restricted.html')

# Logout view restricted to authenticated users
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('pantry:index'))

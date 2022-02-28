from django import forms
from django.contrib.auth.models import User
from pantry.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # No fields need to be set at sign up
        fields = ()

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)

class recipeForm(forms.ModelForm):
	name = forms.CharField(max_length, help_text="Please enter the recipe name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Recipe
		fields = ('name',)
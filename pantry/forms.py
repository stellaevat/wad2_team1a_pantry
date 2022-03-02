from django import forms
from django.forms import TextInput, EmailInput
from django.contrib.auth.models import User
from pantry.models import UserProfile, Recipe

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'login-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'login-input'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'login-input'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match")
            
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # No fields need to be set at sign up
        fields = ()

class EmailForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'Enter email', 'class': 'login-input'}))
    
    class Meta:
        model = User
        fields = ('email',)

class RecipeForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the recipe name.")
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)
	
	class Meta:
		model = Recipe
		fields = ('name',)
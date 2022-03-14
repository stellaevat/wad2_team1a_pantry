from django import forms
from django.forms import TextInput, EmailInput, NumberInput, ClearableFileInput
from django.contrib.auth.models import User
from pantry.models import UserProfile, Recipe, Category, IngredientList
from pantry.custom_widgets import ColumnCheckboxSelectMultiple


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username', 'class': 'login-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'login-input'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'login-input'}))
    
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')
        
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match.")
            
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
    # Add blank default for difficulty
    DIFFICULTIES = [('', '--------')]
    DIFFICULTIES.extend(list(Recipe.get_difficulties()))
    DIFFICULTIES = tuple(DIFFICULTIES)
    
    title = forms.CharField(max_length=128, help_text="Recipe title: ",
            widget=TextInput(attrs={"class":"long-info"}))
    picture = forms.ImageField(help_text="Recipe photo: ",
              widget=ClearableFileInput(attrs={"class":"picture-upload"}))
    prep_time = forms.IntegerField(help_text="Preparation time (mins): ",
                widget=NumberInput(attrs={"class":"short-info"}))
    cook_time = forms.IntegerField(help_text="Cooking time (mins): ",
                widget=NumberInput(attrs={"class":"short-info"}))
    difficulty = forms.ChoiceField(help_text="Difficulty: ", choices=DIFFICULTIES)
    servings = forms.IntegerField(help_text="Servings: ",
               widget=NumberInput(attrs={"class":"short-info"}))
    steps = forms.CharField(max_length=2048, help_text="Method: ", widget=forms.Textarea(attrs={"id":"method-input"}), required=True)
    # Custom widget to display checkboxes in columns
    category = forms.ModelMultipleChoiceField(help_text="Categories: ", queryset=Category.objects.all(), required=False,
               widget=ColumnCheckboxSelectMultiple(columns=3, class_whole="checkbox-area",
               class_column="checkbox-column", separator="gap", attrs={"class":"checkbox"}))
    
    class Meta:
        model = Recipe
        exclude = ('stars', 'slug', 'ingredients', 'author', 'pub_date')
            
class RecipeIngredientsForm(forms.ModelForm):
    ingredients = forms.CharField(max_length=128, help_text="Please add some ingredients.", required=False)
    class Meta:
        model = Recipe
        fields = ('ingredients',)

class RecipeQuantitesForm(forms.ModelForm):
    quantity = forms.CharField(max_length=20,required=False)
    plural = forms.BooleanField(required=False)
    class Meta:
        model = IngredientList
        fields = ('quantity', 'plural',)
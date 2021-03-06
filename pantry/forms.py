from django import forms
from django.forms import TextInput, EmailInput, NumberInput, PasswordInput, ClearableFileInput
from django.contrib.auth.forms import PasswordChangeForm
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
        username = cleaned_data.get("username")

        if len(password) < 8:
            self.add_error('password', "Password too short - it must contain at least 8 characters.")
        elif password.isnumeric():
            self.add_error('password', "Password too simple - it must contain more than just numeric characters.")
        elif password.lower() == username.lower():
            self.add_error('password', "Username and password too similar - try something different.")
        elif password != confirm_password:
            self.add_error('confirm_password', "Passwords don't match - please try again.")
        
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # Email already submitted at check_email stage, nothing new to submit
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
              widget=ClearableFileInput(attrs={"class":"picture-upload","id":"recipe-pic-upload"}))
    prep_time = forms.IntegerField(help_text="Preparation time (mins): ",
                widget=NumberInput(attrs={"class":"short-info"}))
    cook_time = forms.IntegerField(help_text="Cooking time (mins): ",
                widget=NumberInput(attrs={"class":"short-info"}))
    difficulty = forms.ChoiceField(help_text="Difficulty: ", choices=DIFFICULTIES)
    servings = forms.IntegerField(help_text="Servings: ",
               widget=NumberInput(attrs={"class":"short-info"}))
    steps = forms.CharField(max_length=2048, help_text="Method: ", widget=forms.Textarea(attrs={"id":"method-input"}), required=True)
    # Custom widget to display checkboxes in columns
    category = forms.ModelMultipleChoiceField(help_text="Categories: ", queryset=Category.objects.filter(selectable=True), required=False,
               widget=ColumnCheckboxSelectMultiple(columns=3, class_whole="checkbox-area",
               class_column="checkbox-column", separator="gap", attrs={"class":"checkbox"}))
    
    class Meta:
        model = Recipe
        exclude = ('stars', 'slug', 'ingredients', 'author', 'pub_date')
            
class RecipeIngredientsForm(forms.ModelForm):
    ingredients = forms.CharField(max_length=20, help_text="Please add some ingredients.", required=False)
    class Meta:
        model = Recipe
        fields = ('ingredients',)

class RecipeQuantitesForm(forms.ModelForm):
    quantity = forms.CharField(max_length=20,required=False)
    plural = forms.BooleanField(required=False)
    class Meta:
        model = IngredientList
        fields = ('quantity', 'plural',)

class EditProfilePicture(forms.ModelForm):
    profile_picture = forms.ImageField(widget=ClearableFileInput(attrs={"class":"picture-upload"}))

    def is_valid(self,request):
        # Image file types widely supported by web browsers
        accepted_exts = ['bmp', 'cur', 'gif', 'png', 'apng', 'ico',
                         'jfif', 'jpe', 'jpg', 'jpeg', 'webp']
        if 'profile_picture' in request.FILES:
            ext = request.FILES["profile_picture"].name.split(".")[-1]
            if ext in accepted_exts:
                return True
            else:
                self.add_error('profile_picture', 'Invalid file format - please select an image.')
        elif 'profile_picture-clear' in request.POST:
            return True
        else:
            self.add_error('profile_picture', 'No file chosen. To clear your profile picture please choose Clear.')
        return False

    class Meta:
        model = UserProfile
        fields = ('profile_picture',)


class EditUsername(forms.ModelForm):
    username = forms.CharField(max_length=128, help_text="Username: ", widget=TextInput(attrs={"placeholder":"New username", }))
    class Meta:
        model = User
        fields = ('username',)

class EditEmail(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text="Email: ", widget=TextInput(attrs={"placeholder":"New email",}), required=True)
    class Meta:
        model = UserProfile
        fields = ('email',)

class EditPassword(PasswordChangeForm):
    old_password = forms.CharField(max_length=128, widget=PasswordInput(attrs={'placeholder':'Old password'}))
    new_password1 = forms.CharField(max_length=128, widget=PasswordInput(attrs={'placeholder':'New password'}))
    new_password2 = forms.CharField(max_length=128, widget=PasswordInput(attrs={'placeholder':'Confirm password'}))
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)
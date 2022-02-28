from django.contrib import admin
from pantry.models import UserProfile, User, Category, Ingredient, Recipe

admin.site.register(UserProfile)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)

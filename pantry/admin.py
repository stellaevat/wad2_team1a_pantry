from django.contrib import admin
from pantry.models import UserProfile, SiteUser, Category, Ingredient, Recipe

admin.site.register(UserProfile)
admin.site.register(SiteUser)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)

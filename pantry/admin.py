from django.contrib import admin
from pantry.models import UserProfile, Category, Ingredient, Recipe, IngredientList

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
# Id is of interest when search by ingredient / adding recipe ingredients, in case of error
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredient_type', 'id')

admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientList)

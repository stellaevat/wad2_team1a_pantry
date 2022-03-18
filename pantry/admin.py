from django.contrib import admin
from pantry.models import UserProfile, Category, Ingredient, Recipe, IngredientList

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email',)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'tab')
    
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'author', 'pub_date', 'stars')
    
# Id is of interest when resolving issues with search by ingredient / adding recipe ingredients
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredient_type', 'id')
    
class IngredientListAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'ingredient', 'quantity', 'plural')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientList, IngredientListAdmin)

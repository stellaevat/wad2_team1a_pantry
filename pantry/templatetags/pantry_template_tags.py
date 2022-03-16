import os
from os.path import exists
from pathlib import Path
from django import template
from pantry.models import Category, Recipe, IngredientList, UserProfile
register = template.Library()

@register.inclusion_tag('pantry/tabs.html')
def get_tabs(current_tab=None):
    return {'tabs': Category.objects.filter(tab=True), 'current_tab': current_tab}
    
@register.inclusion_tag('pantry/recipe_grid_display.html')
def recipe_grid_display(recipe, small=False, percent=None):
    size = "small" if small else "big"   
    return {'recipe': recipe,
            'size': size,
            'time': recipe.prep_time + recipe.cook_time,
            'percent': percent,}
 
@register.inclusion_tag('pantry/recipe_sorter.html') 
def get_recipe_sorter(sort_type=None, by_ingredient=False):
    return {'sort_type': sort_type,
            'by_ingredient': by_ingredient}

@register.inclusion_tag('pantry/categories_dropdown.html')
def get_categories_dropdown():
    return {'tabs': Category.objects.filter(tab=True),
            'categories': Category.objects.filter(tab=False)}
    
@register.inclusion_tag('pantry/ingredient_selection.html')
def get_ingredient_selection(types, ingredients):
    return {'types': types, 'ingredients': ingredients,}
    
@register.filter
def get_profile_picture(user):
    try:
        user_profile = UserProfile.objects.get(user=user)
        return user_profile.profile_picture
    except:
        return None

@register.filter
def check_if_starred(user,recipe):
    try:
        user_profile = UserProfile.objects.get(user=user)
        if recipe in Recipe.objects.filter(users=user_profile):
            return True
        else:
            return False
    except:
        return False
    
@register.filter
def get_recipes_by_author(user):
    return Recipe.objects.filter(author=user)
    
@register.filter
def get_item(iterable, key):
    try:
        return iterable[key]
    except:
        return ""
    
@register.filter
def get_number(ingredient, plural):
    if plural:
        return ingredient.get_plural()
    else:
        return ingredient.name

@register.filter
def format_time(mins, short=False):
    time = ""
    min_marker = " '" if short else " min"
 
    hours = int(mins / 60)
    mins = mins % 60
    if hours:
        time += str(hours) + " h "
    if mins:
        time += str(mins) + min_marker
            
    if time:
        return time
    else:
        return "0" + min_marker
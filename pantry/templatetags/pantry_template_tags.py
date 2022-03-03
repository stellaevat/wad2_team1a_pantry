from django import template
from pantry.models import Category, Recipe, UserProfile
register = template.Library()

@register.inclusion_tag('pantry/tabs.html')
def get_tabs(current_tab=None):
    return {'tabs': Category.objects.filter(tab=True)}
    
@register.filter
def get_profile_picture(user):
    user_profile = UserProfile.filter(user=user)
    return user_profile.profile_picture
    
@register.filter
def get_recipes_by_author(user):
    return Recipe.objects.filter(author=user)
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
    
# Recipe thumbnail, include new paras, dropdown display(?)
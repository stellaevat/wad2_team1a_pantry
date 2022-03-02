from django import template
from pantry.models import Category
register = template.Library()

@register.inclusion_tag('pantry/tabs.html')
def get_tabs(current_tab=None):
    return {'tabs': Category.objects.filter(tab=True)}
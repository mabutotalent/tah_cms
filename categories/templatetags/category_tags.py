from django import template

from categories.models import Category

register = template.Library()

@register.simple_tag
def get_category_tag():
    return Category.objects.all()
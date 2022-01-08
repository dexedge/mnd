from django import template

register = template.Library()

@register.simple_tag
def new_year(new_value):
    return new_value
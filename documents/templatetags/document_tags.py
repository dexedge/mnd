from django import template

register = template.Library()

@register.simple_tag
def new_year(new_value):
    return new_value

# Strip <p> tags
# @register.simple_tag
# def clean(self):
#     return re.findall(r'>(.*?)</p>', self)[0]
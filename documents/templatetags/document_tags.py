from django import template
from documents.models import DocumentPage, Author

register = template.Library()

@register.simple_tag
def new_year(new_value):
    return new_value

@register.simple_tag
def document_count():
    return DocumentPage.objects.all().count()

# @register.inclusion_tag("top/author.html", takes_context=True)
# def authors(context):
#     return {
#         'authors': Author.objects.all(),
#         'request': context['request'],
#     }

# Strip <p> tags
# @register.simple_tag
# def clean(self):
#     return re.findall(r'>(.*?)</p>', self)[0]
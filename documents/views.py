from django.views.generic import DetailView
from documents.models import Author, DocumentPage

class AuthorDetail(DetailView):
    context_object_name = 'author'
    model = Author
    template_name = "documents/author_detail.html"

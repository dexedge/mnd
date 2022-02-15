from django.views.generic import DetailView
from documents.models import Author

class AuthorDetail(DetailView):
    context_object_name = 'author'
    model = Author
    template_name = "documents/author_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
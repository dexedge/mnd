from django.views.generic import DetailView
from documents.models import Author, DocumentPage
from news.models import NewsPage
from datetime import date

from django_renderpdf.views import PDFView

class AuthorDetail(DetailView):
    context_object_name = 'author'
    model = Author
    template_name = "documents/author_detail.html"

class DocumentPDF(PDFView):
    template_name = "documents/document_pdf.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        page = DocumentPage.objects.get(slug = kwargs['slug'])
        now = date.today()
        today = now.strftime("%a, %d %b %Y")
        context["today"] = today

        context["page"] = page
       
        # Build author names

        authors = page.authors.all()
        context["authors"] = authors
        if authors.count() == 1:
            context["author_heading"] = "Author"
            context["author_names"] = authors.first().author.full_name
            author_surnames = authors.first().author.last_name
            context["author_surnames"] = author_surnames
            context["citation_names"] = authors.first().author
        else:
            context["author_heading"] = "Authors"
            author_names = authors.first().author.full_name
            author_surnames = authors.first().author.last_name
            citation_names = authors.first().author.last_name + ", "  + authors.first().author.first_names
            for i in range(1, len(authors)):
                if i == (len(authors) - 1):
                    author_names = author_names + " and " + authors[i].author.full_name
                    author_surnames = author_surnames + " & " + authors[i].author.last_name
                    citation_names = citation_names + ", and " + authors[i].author.full_name
                else:
                    author_names = author_names + ", " + authors[i].author.full_name
                    author_surnames = author_surnames + ", " + authors[i].author.last_name
                    citation_names = citation_names + ", " + authors[i].author.full_name
            
            context["author_names"] = author_names
            context["author_surnames"] = author_surnames
            context["citation_names"] = citation_names
            
    
        return(context)
    
class NewsPDF(PDFView):
    template_name = "news/news_page_pdf.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        page = NewsPage.objects.get(slug = kwargs['slug'])
        now = date.today()
        today = now.strftime("%a, %d %b %Y")
        context["today"] = today

        context["page"] = page

        return(context)

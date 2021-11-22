from django.db import models

from documents.models import DocumentPage

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class TopLevelPage(Page):
    parent_page_types = ["home.HomePage"]
    template = "top/top_level_page.html"

    top_level_text = RichTextField(
        blank=True,
        features=['h1', 'h2', 'bold', 'italic', 'blockindent', 'ul', 'image', 'link', 'hr'],
    )

    updated = models.DateField("Updated", blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("top_level_text"),
        FieldPanel("updated")
    ]

class IndexPage(Page):
    parent_page_types = ["home.HomePage"]
    template = "top/index_page.html"

    body = RichTextField(
        blank=True,
        features=['h1', 'h2','h3', 'bold', 'italic', 'underline','blockindent', 'image', 'link', 'hr'],
    )

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

class CategoryListingPage(Page):
    template = "categories.html"
    max_count = 1
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        documents = DocumentPage.objects.public().order_by("categories", "date")
        context["biography"] = documents.filter(categories__name="Biography")
        context["reception"] = documents.filter(categories__name="Reception")
        context["literature"] = documents.filter(categories__name="Mozart in Literature")
        
        return context
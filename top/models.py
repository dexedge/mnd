from django.db import models

from documents.models import DocumentPage

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

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

    body = StreamField([
        ('year_or_kv', blocks.CharBlock(
            template="streams/h2.html", 
            required=True,
            help_text='Year or Köchel number'
        )),
        ('page', blocks.RichTextBlock(
            template="streams/page.html",
            features=['italic', 'link'],
        )),
        
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
    
    def prev(self):
        prev_sibling = self.get_prev_sibling()
        
        if not prev_sibling.title=="Abbreviations":
            return prev_sibling.url
    
    def next(self):
        if self.get_next_sibling():
            return self.get_next_sibling().url

class CategoryListingPage(Page):
    parent_page_types = ["home.HomePage"]
    template = "top/categories.html"
    max_count = 1
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        documents = DocumentPage.objects.public().order_by("categories", "date")
        context["biography"] = documents.filter(categories__name="Biography")
        context["reception"] = documents.filter(categories__name="Reception")
        context["literature"] = documents.filter(categories__name="Mozart in Literature")
        
        return context

    def prev(self):
        return self.get_prev_sibling().url
    
    def next(self):
        return self.get_next_sibling().url
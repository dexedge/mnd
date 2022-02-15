from django.db import models

from documents.models import DocumentPage, KoechelNumber

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

# Abbrevations #
class Heading(blocks.StructBlock):
    heading = blocks.CharBlock(
        max_length = 100,
        required=False,
    )

    class Meta:
        template = "streams/abbreviation-heading.html"

class Subheading(blocks.StructBlock):
    subheading = blocks.CharBlock(
        max_length = 100,
        required=False,
    )

    class Meta:
        template = "streams/abbreviation-subheading.html"

class Abbreviation(blocks.StructBlock):
        abbreviation = blocks.RichTextBlock(
            features = ["italic", "underline"],
            form_classname="abbreviation",
        )
        link_id = blocks.CharBlock(
            help_text='For making hyperlinks to this heading'
        )
        reference = blocks.RichTextBlock(
            features = ["italic", "underline", "link"]
        )
        
        class Meta:
            template = 'streams/abbreviation.html'

class AbbreviationsPage(Page):
    parent_page_types = ["home.HomePage"]
    template = "top/abbreviations.html"
    max_count = 1

    abbreviations = StreamField([
        ("heading", Heading(
            icon='edit',
            label="Heading"
        )),
        ("subheading", Subheading(
            icon='edit',
            label="Subheading"
        )),
        ("item", Abbreviation(
            icon='edit', 
            label="Abbreviation"
        )),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("abbreviations"),
    ]

# Index Pages
class IndexPage(Page):
    parent_page_types = ["home.HomePage"]
    template = "top/index_page.html"

    body = StreamField([
        ('year', blocks.CharBlock(
            template="streams/h2.html", 
            required=True,
            help_text='Year'
        )),
        ('page', blocks.RichTextBlock(
            template="streams/page.html",
            features=['italic', 'link'],
        )),
        
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
    
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
        context["advertisement"] = documents.filter(categories__name="Advertisement")
        context["addenda"] = documents.filter(categories__name="Addenda")
        context["corrigenda"] = documents.filter(categories__name="Corrigenda")
        
        return context

class KoechelListingPage(Page):
    parent_page_types = ["home.HomePage"]
    template = "top/koechel.html"
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["koechel_numbers"] = KoechelNumber.objects.all()
        
        return context



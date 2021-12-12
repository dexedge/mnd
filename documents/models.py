from django.db import models
from django import forms
from django.db.models.expressions import F

from modelcluster.fields import ParentalManyToManyField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet

# new_table_options = {
#     'minSpareRows': 0,
#     'startRows': 2,
#     'startCols': 3,
#     'colHeaders': False,
#     'rowHeaders': False,
#     'contextMenu': True,
#     'editor': 'text',
#     'stretchH': 'all',
#     'height': 216,
#     'language': 'en',
#     'renderer': 'html',
#     'autoColumnSize': False,
# }

full_features_list = ['h1', 'h2','h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed']

class Heading(blocks.StructBlock):
    heading = blocks.CharBlock(classname='full title')
    link_id = blocks.CharBlock(help_text='For making hyperlinks to this heading')

    class Meta:
        template = 'streams/heading.html' 

class DocumentPage(Page):
    template  = "documents/document.html"
    parent_page_types = ["top.IndexPage"]
    
    date = models.DateField("Date", null=True, blank=True)
    document_title = RichTextField(
        blank=True,
        features=['italic', 'underline', 'h1'],
        help_text="Field must be manually marked as h1",
    )
    source = RichTextField(
        blank=True,
        features=['italic', 'underline', 'h2'],
        help_text="Field must be manually marked as h2",
    )
    source_image = StreamField([
        ('large_image', ImageChooserBlock(
            help_text="Source image",
        )),
    ], null=True, blank=True)
    transcription = RichTextField(
        blank=True,
        features=full_features_list,
    )
    translation = RichTextField(
        blank=True,
        features=full_features_list,
    )
    commentary = StreamField([
        ("richtext", blocks.RichTextBlock(
            template="streams/richtext_block.html",
            features=full_features_list,
        )),
        ("heading", Heading()),
        ("table", TypedTableBlock([
                ('text', blocks.CharBlock()),
                ('numeric', blocks.FloatBlock()),
                ('rich_text', blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link', 'h2'],)),
            ],
        )),
    ], null=True, blank=True)
    
    notes = StreamField([
        ("richtext", blocks.RichTextBlock(
            template="streams/richtext_block.html",
            features=full_features_list,
        )),
        ("table", TypedTableBlock([
                ('text', blocks.CharBlock()),
                ('numeric', blocks.FloatBlock()),
                ('rich_text', blocks.RichTextBlock(features=['italic', 'bold', 'strikethrough', 'link', 'h2'],)),
            ],
        )),
    ], null=True, blank=True)
    bibliography = RichTextField(
        blank=True,
        features=full_features_list,
    )
    credit = models.CharField(max_length=100, blank=True)
    repository = models.CharField(max_length=100, blank=True)
    repository_link = models.URLField(null=True, blank=True)
    search_term = models.CharField(max_length=100, blank=True)
    source_library = models.CharField(max_length=100, blank=True)
    categories = ParentalManyToManyField(
        "documents.DocumentCategory", blank=True
    )
    author = models.CharField(max_length=200, blank=True)
    citation_title = models.TextField(
        help_text="Field allows HTML tagging",
        blank=True
    )
    first_published = models.DateField(null=True, blank=True)
    updated = models.DateField(null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("document_title"),
        FieldPanel("source"),
        StreamFieldPanel("source_image"),
        FieldPanel("transcription"),
        FieldPanel("translation"),
        StreamFieldPanel("commentary"),
        StreamFieldPanel("notes"),
        FieldPanel("bibliography"),
        FieldPanel("credit"),
        FieldPanel("repository"),
        FieldPanel("repository_link"),
        FieldPanel("search_term"),
        FieldPanel("source_library"),
        MultiFieldPanel(
            [FieldPanel("categories", widget=forms.CheckboxSelectMultiple)],
            heading="Categories"
        ),
        FieldPanel("author"),
        FieldPanel("citation_title"),
        FieldPanel("first_published"),
        FieldPanel("updated"),
    ]

    class Meta:
        ordering = ("date",)
    
    def prev(self):
        prev_sibling = self.get_prev_sibling()
        prev_parent_last = self.get_parent().get_prev_sibling().get_children().last()
        if prev_sibling:
            return prev_sibling.url
        elif prev_parent_last:
            return prev_parent_last.url
    
    def next(self):
        next_sibling = self.get_next_sibling()
        next_parent_first = self.get_parent().get_next_sibling().get_children().first()
        if next_sibling:
            return next_sibling.url
        elif next_parent_first:
            return next_parent_first.url
            
    
@register_snippet
class DocumentCategory(models.Model):
    """Document category for a snippet."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify posts in this category',
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        # ordering = ["name"]

    def __str__(self):
        return self.name
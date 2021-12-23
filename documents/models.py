from django.db import models
from django import forms
from django.db.models.expressions import F
from django.db.models.fields import related
from datetime import datetime
import re

from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, FieldRowPanel
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

full_features_list = ['h1', 'h2','h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red','blue', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed']

class Heading(blocks.StructBlock):
    heading = blocks.CharBlock(classname='full-title')
    link_id = blocks.CharBlock(help_text='For making hyperlinks to this heading')

    class Meta:
        template = 'streams/heading.html'

class Caption(blocks.StructBlock):
    caption = blocks.RichTextBlock(
        features=['italic', 'bold', 'strikethrough', 'link'],
        form_classname='centered'
        )

    class Meta:
        template = 'streams/caption.html'

class Centered(blocks.StructBlock):
    text = blocks.RichTextBlock(
        features=['italic', 'bold', 'strikethrough', 'link'],
        form_classname='centered'
    )

    class Meta:
        template = 'streams/centered.html'

class MultipleImages(blocks.StructBlock):
    images = blocks.RichTextBlock(
        features=['image']
    )

    class Meta:
        template = 'streams/images.html'

class DocumentPage(Page):
    template  = "documents/document.html"
    parent_page_types = ["top.IndexPage"]
    
    date = models.DateField("Date", null=True)
    date_precision = models.CharField(
        max_length=10,
        
        choices=(
            ("full", "Full"),
            ("month", "Month"),
            ("year", "Year")
        ), default="full", null=True
    )
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
        ("heading", Heading(icon='title')),
        ("caption", Caption(icon='edit')),
        ("table", TypedTableBlock([
                ('text', blocks.CharBlock(required=False)),
                ('numeric', blocks.FloatBlock(required=False)),
                ('rich_text', blocks.RichTextBlock(
                    required=False,
                    features=['italic', 'bold', 'strikethrough', 'red','link', 'h2'],)),
            ],
        )),
        ('centered_text', Centered(icon="edit")),
        ('images', MultipleImages(icon='image')),
    ], null=True, blank=True)
    
    notes = StreamField([
        ("richtext", blocks.RichTextBlock(
            template="streams/richtext_block.html",
            features=full_features_list,
        )),
        ("table", TypedTableBlock([
                ('text', blocks.CharBlock(required=False)),
                ('numeric', blocks.FloatBlock(required=False)),
                ('rich_text', blocks.RichTextBlock(
                    required=False,
                    features=['italic', 'bold', 'strikethrough','red', 'link', 'h2'],)),
            ],
        )),
    ], null=True, blank=True)
    bibliography = RichTextField(
        blank=True,
        features=full_features_list,
    )
    credit = models.CharField(max_length=100, blank=True)
    source_link = RichTextField(
        blank=True,
        features=['italic', 'bold', 'link',],
    )
    search_term = models.CharField(max_length=100, blank=True)
    source_library = RichTextField(
        blank=True,
        features=['italic', 'bold', 'link',],
    )
    categories = ParentalManyToManyField(
        "documents.DocumentCategory", blank=True
    )
    author = models.CharField(max_length=200, blank=True)
    first_published = models.DateField(null=True, blank=True)
    updated = models.DateField(null=True, blank=True)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("date"),
            FieldPanel("date_precision", widget=forms.RadioSelect()),
        ], heading="Date"),
        FieldPanel("document_title"),
        FieldPanel("source"),
        StreamFieldPanel("source_image"),
        FieldPanel("transcription"),
        FieldPanel("translation"),
        StreamFieldPanel("commentary"),
        StreamFieldPanel("notes"),
        FieldPanel("bibliography"),
        FieldPanel("credit"),
        # InlinePanel("source_link", label="Source Links"),
        FieldPanel('source_link'),
        FieldPanel("search_term"),
        FieldPanel("source_library"),
        MultiFieldPanel(
            [FieldPanel("categories", widget=forms.CheckboxSelectMultiple)],
            heading="Categories"
        ),
        FieldPanel("author"),
        FieldPanel("first_published"),
        FieldPanel("updated"),
    ]

    class Meta:
        ordering = ("date",)
    
    @property
    def display_date(self):
        if self.date_precision=="full":
            return self.date.strftime("%-d %b %Y")
        elif self.date_precision=="month":
            return self.date.strftime("%b %Y")
        else:
            return self.date.strftime("%Y")

    # Strip <h1> tag from document_title
    @property
    def clean_title(self):
        temp = self.document_title
        temp = re.findall(r'>(.*?)</h1>', temp)[0]
        return temp

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

# DEPRECATED
# class SourceLink(models.Model):
#     source_link = RichTextField(
#         blank=True,
#         features=['italic', 'bold', 'link',],
#     )

#     panels = [
#         FieldPanel('source_link'),
#     ]

#     class Meta:
#         abstract = True

# class DocumentPageSourceLinks(Orderable, SourceLink):
#     page = ParentalKey(
#         'documents.DocumentPage',
#         on_delete=models.CASCADE,
#         related_name='source_link'
#     )
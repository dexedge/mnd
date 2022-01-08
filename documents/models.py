from django.db import models
from django import forms
from django.utils.html import strip_tags
from django.shortcuts import render 
import re

from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.contrib.typed_table_block.blocks import TypedTableBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.search import index

# Features list for Draftail editor
full_features_list = ['h1', 'h2','h3', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red','blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'center', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed']

#######################
# Custom StructBlocks #
#######################
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

class ImagesAndCaption(blocks.StructBlock):
    images = blocks.RichTextBlock(
        features=['image']
    )
    caption = blocks.RichTextBlock(
        features=['italic', 'bold', 'strikethrough', 'link'],
        form_classname='centered',
        required=False
        )

    class Meta:
        template = 'streams/images.html'

class Centered(blocks.StructBlock):
    text = blocks.RichTextBlock(
        features=['italic', 'bold', 'strikethrough', 'link'],
        form_classname='centered'
    )

    class Meta:
        template = 'streams/centered.html'

#################
# Document Page #
#################

class DocumentPage(Page):
    template  = "documents/document.html"
    parent_page_types = ["top.IndexPage", "DocumentList"]
    
    date = models.DateField("Date", null=True)
    date_precision = models.CharField(
        max_length=10,
        choices=(
            ("full", "Full"),
            ("month", "Month"),
            ("year", "Year"),
            ("custom", "Custom")
        ), default="full", null=True
    )
    date_custom = models.CharField(
        max_length=100,
        help_text="Use only for date ranges",
        blank=True,
        null=True
    )
    document_title = RichTextField(
        blank=True,
        features=['italic', 'underline'],
    )
    source = RichTextField(
        blank=True,
        features=['italic', 'underline'],
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
        ('images', ImagesAndCaption(icon='image', label="Images with Caption")),
        ("caption", Caption(icon='edit', label="Generic Caption")),
        ("table", TypedTableBlock([
                ('text', blocks.CharBlock(required=False)),
                ('numeric', blocks.FloatBlock(required=False)),
                ('rich_text', blocks.RichTextBlock(
                    required=False,
                    features=['italic', 'bold', 'strikethrough', 'red','link', 'h2'],)),
            ],
        )),
        ('centered_text', Centered(icon="edit")),
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
            FieldPanel("date_custom"),
        ], heading="Date"),
        FieldPanel("document_title", classname="title"),
        FieldPanel("source", classname="source"),
        StreamFieldPanel("source_image"),
        FieldPanel("transcription"),
        FieldPanel("translation"),
        StreamFieldPanel("commentary"),
        StreamFieldPanel("notes"),
        FieldPanel("bibliography"),
        FieldPanel("credit"),
        FieldPanel('source_link'),
        FieldPanel("search_term"),
        FieldPanel("source_library"),
        MultiFieldPanel(
            [FieldPanel("categories", widget=forms.CheckboxSelectMultiple)],
            heading="Categories"
        ),
        MultiFieldPanel([
            InlinePanel("koechel_numbers", label="Köchel Number")
        ], heading="Köchel Numbers"),
        FieldPanel("author"),
        FieldPanel("first_published"),
        FieldPanel("updated"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('title'),
        index.SearchField('document_title'),
        index.SearchField('source'),
        index.SearchField('transcription'),
        index.SearchField('commentary'),
        index.SearchField('notes'),
        index.SearchField('bibliography'),
        index.SearchField('author'),
    ]

    class Meta:
        ordering = ("date",)
    
    @property
    def display_date(self):
        if self.date_precision=="full":
            return self.date.strftime("%-d %b %Y")
        elif self.date_precision=="month":
            return self.date.strftime("%b %Y")
        elif self.date_precision=="year":
            return self.date.strftime("%Y")
        else:
            if self.date_custom:
                return self.date_custom
            else:
                return "NO DATE"
    
    @property
    def index_date(self):
        if self.date_precision=="full":
            return self.date.strftime("%-d %b")
        elif self.date_precision=="month":
            return self.date.strftime("%b")
        elif self.date_precision=="year":
            return None
        else:
            if self.date_custom:
                return self.date_custom
            else:
                return "NO DATE"
    
    @property
    def year(self):
        return self.date.year
   
    # Strip <p> tag from document_title
    @property
    def clean_title(self):
        temp = self.document_title
        temp = re.findall(r'>(.*?)</p>', temp)[0]
        return temp
    
    # Strip <p> tag from source
    @property
    def clean_source(self):
        temp = self.source
        temp = re.findall(r'>(.*?)</p>', temp)[0]
        return temp

    def prev(self):
        prev_sibling = self.get_prev_sibling()
        if prev_sibling:
            return prev_sibling.url
        
    def next(self):
        next_sibling = self.get_next_sibling()
        if next_sibling:
            return next_sibling.url


#################
# Document List #
#################

class DocumentList(RoutablePageMixin, Page):
    parent_page_types = ["home.HomePage"]
    template = "documents/document_list.html"
    
    @route(r'^1760-1779/$')
    def index_1760_to_1779 (self, request):
        context = self.get_context(request)
        context['range'] = "1760&ndash;1779"
        context['documents'] = DocumentPage.objects.filter(date__year__lt=1780)
        return render(request, "documents/document_list.html", context)
    
    @route(r'^1780-1787/$')
    def index_1780_to_1787 (self, request):
        context = self.get_context(request)
        context['range'] = "1780&ndash;1787"
        context['documents'] = DocumentPage.objects.filter(date__year__gte=1780, date__year__lt=1788)
        return render(request, "documents/document_list.html", context)
    
    @route(r'^1788-1793/$')
    def index_1788_to_1793 (self, request):
        context = self.get_context(request)
        context['range'] = "1788&ndash;1793"
        context['documents'] = DocumentPage.objects.filter(date__year__gt=1787)
        return render(request, "documents/document_list.html", context)

#####################
# Document Category #
#####################
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

##################
# Koechel Number #
##################
@register_snippet
class KoechelNumber(models.Model):
    koechel_display = models.CharField(max_length=25)
    koechel_sortable = models.CharField(max_length=25)
    koechel_alternate = models.CharField(
        max_length=25, 
        blank=True,
        null=True)
    koechel_title = RichTextField(
        features=['bold', 'italic',],
        blank=True, null=True)

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('koechel_display', heading="KV"),
                FieldPanel('koechel_sortable', heading="Sortable"),
                FieldPanel('koechel_alternate', heading="Alternate"),
            ]),
            FieldPanel('koechel_title', heading="Uniform Title"),
        ], heading="Köchel Number",),

    ]

    def __str__(self):
        temp = strip_tags(self.koechel_title)
        temp = temp.replace("&quot;", '"')
        return self.koechel_display + ": " + temp

    # Strip <p> tag from koechel_title
    @property
    def clean_title(self):
        temp = self.koechel_title
        temp = re.findall(r'>(.*?)</p>', temp)[0]
        return temp

    class Meta:
        ordering=("koechel_sortable",)
        verbose_name = "Koechel Number"
        verbose_name_plural = "Koechel Numbers"

class KoechelNumberOrderable(Orderable):
    page = ParentalKey("documents.DocumentPage", related_name="koechel_numbers")
    koechel_number = models.ForeignKey(
        "documents.KoechelNumber",
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("koechel_number")
    ]
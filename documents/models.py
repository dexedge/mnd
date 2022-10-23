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

from wagtail_pdf_view.mixins import PdfViewPageMixin

# Features list for Draftail editor
full_features_list = ['h1', 'h2','h3', 'h4', 'bold', 'italic', 'underline', 'strikethrough', 'small', 'red','blue', 'green', 'blockquote', 'blockindent', 'doubleindent', 'superscript', 'subscript', 'ul', 'image', 'link', 'hr', 'embed']

#######################
# Custom StructBlocks #
#######################
class Transcription(blocks.StructBlock):
    transcription_text = blocks.RichTextBlock(
        features=full_features_list,
    )
    source_image = ImageChooserBlock(
        help_text="Source image",
        required=False
    )
    
    class Meta: 
        template = 'streams/transcription.html'

class Heading(blocks.StructBlock):
    heading = blocks.RichTextBlock(
        features=['italic', 'bold', 'strikethrough', 'link'],classname='full-title')
    link_id = blocks.CharBlock(
        help_text='For making hyperlinks to this heading')

    class Meta:
        template = 'streams/heading.html'

class Caption(blocks.StructBlock):
    caption = blocks.RichTextBlock(
        features=['italic', 'bold', 'strikethrough', 'link'],
        form_classname='centered'
        )

    class Meta:
        template = 'streams/caption.html'

class Annotation(blocks.StructBlock):
    annotation = blocks.RichTextBlock(
        features=full_features_list,
        form_classname='centered-annotation'
    )

    class Meta:
        template = 'streams/annotation.html'

class LeftJustifiedBlock(blocks.StructBlock):
    left_justified_block = blocks.RichTextBlock(
        features=full_features_list,
        form_classname='left-justified-block'
    )

    class Meta:
        template = 'streams/left-justified-block.html'


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
        features=['italic', 'bold', 'strikethrough', 'superscript', 'subscript','link'],
        form_classname='centered'
    )

    class Meta:
        template = 'streams/centered.html'

class Reference(blocks.StructBlock):
    reference = blocks.RichTextBlock(
        features=['italic', 'bold', 'red', 'strikethrough', 'link']
    )
    link_id = blocks.CharBlock(help_text='For making hyperlinks to this heading')

    class Meta:
        template = 'streams/reference.html'

#################
# Document Page #
#################

class DocumentPage(PdfViewPageMixin, Page):
    template  = "documents/document.html"
    parent_page_types = ["top.IndexPage", "DocumentList"]

    # HTML first
    ROUTE_CONFIG = [
        ("html", r'^$'),
        ("pdf", r'^pdf/$'),
    ]
    
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
        blank=True, null=True,
        features=['italic', 'underline'],
    )
    transcription = StreamField([
        ('transcription_row', Transcription(icon='edit'))
    ], null=True, blank=True)
    translation = RichTextField(
        blank=True,
        features=full_features_list,
    )
    commentary = StreamField([
        ("richtext", blocks.RichTextBlock(
            template="streams/richtext_block.html",
            features=full_features_list,
        )),
        ('images', ImagesAndCaption(icon='image', label="Image(s) with Caption")),
        ("caption", Caption(icon='edit', label="Generic Caption")),
        ("heading", Heading(icon='title')),
        ("annotation", Annotation(icon='edit', label="Annotation Box")),
        ("left_justified_block", LeftJustifiedBlock(icon='edit', label="Left Justified Block")),
        ("side_by_side", Transcription(icon='edit', label="Transcription with Source")),
        ("table", TypedTableBlock([
                ('text', blocks.CharBlock(required=False)),
                ('numeric', blocks.FloatBlock(required=False)),
                ('rich_text', blocks.RichTextBlock(
                    required=False,
                    features=['italic', 'bold', 'strikethrough', 'red', 'blue', 'green', 'link', 'h2'],)),
            ],
        )),
        ('centered_text', Centered(icon="edit")),
    ], null=True, blank=True)
    
    notes = StreamField([
        ("richtext", blocks.RichTextBlock(
            template="streams/richtext_block.html",
            features=full_features_list,
        )),
        ('images', ImagesAndCaption(icon='image', label="Images with Caption")),
        ("side_by_side", Transcription(icon='edit', label="Transcription with Source")),
        ("table", TypedTableBlock([
                ('text', blocks.CharBlock(required=False)),
                ('numeric', blocks.FloatBlock(required=False)),
                ('rich_text', blocks.RichTextBlock(
                    required=False,
                    features=['italic', 'bold', 'strikethrough', 'superscript', 'subscript', 'red', 'blue', 'link', 'h2'],)),
            ],
        )),
        ("heading", Heading(icon='title')),
        ('centered_text', Centered(icon="edit")),
    ], null=True, blank=True)
    bibliography = StreamField([
        ('reference', Reference(icon='edit', label="Reference"))
    ], null=True, blank=True)
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
        StreamFieldPanel("transcription"),
        FieldPanel("translation"),
        StreamFieldPanel("commentary"),
        StreamFieldPanel("notes"),
        StreamFieldPanel("bibliography"),
        MultiFieldPanel([
            FieldPanel("credit"),
            FieldPanel('source_link'),
            FieldPanel("search_term"),
            FieldPanel("source_library"),
        ], heading="Credits"),
        MultiFieldPanel([
            FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
        ], heading="Categories"),
        MultiFieldPanel([
            InlinePanel("koechel_numbers", label="Köchel Number")
        ], heading="Köchel Numbers"),
        MultiFieldPanel([
            InlinePanel("authors", label="Author")
        ], heading="Author(s)"),
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
    ]

    class Meta:
        ordering = ("date",)

    pdf_base_template = "documents/document_pdf.html"
    stylesheets = ["css/pdf_style.css"]

    def get_context(self, request, mode=None, **kwargs):
        context = super().get_context(request, **kwargs)
        
        if mode == 'pdf':
            context["override_base"] = self.pdf_base_template
        
        # Build author names
        authors = self.authors.all()
        context["authors"] = authors
        if authors.count() == 1:
            context["author_heading"] = "Author"
            context["author_names"] = authors.first().author.full_name
            context["author_surnames"] = authors.first().author.last_name
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

        return context

    @property
    def display_date(self):
        if self.date_precision=="full":
            return self.date.strftime("%-d %b %Y")
        elif self.date_precision=="month":
            return self.date.strftime("%b %Y")
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
            return self.date.strftime("%-d %b")
        elif self.date_precision=="month":
            return self.date.strftime("%b")
        elif self.date_precision=="year":
            return None
        else:
            if self.date_custom[-5] == " ":
                return self.date_custom[0:-5]
            else:
                return self.date_custom
    
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
        if self.source:
            temp = self.source
            temp = re.findall(r'>(.*?)</p>', temp)[0]
            return temp

    # Previous and Next links
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
    
    @route(r'^1788-1829/$')
    def index_1788_to_1829 (self, request):
        context = self.get_context(request)
        context['range'] = "1788&ndash;1829"
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

###########
# Authors #
###########
@register_snippet
class Author(models.Model):
    last_name = models.CharField(max_length = 50)
    first_names = models.CharField(max_length = 50)

    panels = [
        FieldRowPanel([
            FieldPanel('last_name', heading="Last Name"),
            FieldPanel('first_names', heading="First Names"),
        ], heading="Author"),
    ]

    search_fields = Page.search_fields + [
         index.SearchField('last_name'),
         index.SearchField('first_names'),
    ]

    def __str__(self):
        return self.last_name + ", " + self.first_names

    class Meta:
        ordering = ("last_name", "first_names")
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    @property
    def full_name(self):
        return self.first_names + " " + self.last_name


class AuthorOrderable(Orderable):
    page = ParentalKey("documents.DocumentPage", related_name="authors")
    author = models.ForeignKey(
        "documents.Author",
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("author")
    ]


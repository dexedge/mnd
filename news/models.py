from django.db import models
from django.db.models.expressions import F
import re

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, StreamFieldPanel
from wagtail.snippets.models import register_snippet


from documents.models import full_features_list, ImagesAndCaption

class NewsListingPage(Page):
    template = "news/news_listing_page.html"
    max_count = 1
    
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['newspages'] = NewsPage.objects.live().order_by('-date')
        return context

class NewsItem(blocks.StructBlock):
    item = blocks.PageChooserBlock()
    description= blocks.RichTextBlock(
        required=False,
        features=['underline', 'bold', 'italic', 'red', 'blockquote', 'ul', 'hr', 'link']
    )

    class Meta:
        template = 'streams/news_item.html'

class NewsPage(Page):
    template = "news/news_page.html"
    parent_page_types = ["NewsListingPage"]
    
    date = models.DateField("Post date")
    images = StreamField([
        ('news_images', ImagesAndCaption(icon='image', label="Images with Optional Caption")),
    ], blank=True, null=True)
    body = StreamField([
        ('text', blocks.RichTextBlock(
            features=['underline', 'bold', 'italic', 'small', 'red', 'hr', 'blockquote', 'ul', 'link'])
        ),
        ('news_item', NewsItem(icon='edit'))
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('images'),
        FieldPanel('body')  
    ]

    class Meta:
        ordering = ("date",)

    def first_paragraph(self):
        for block in self.body:
            if block.block_type == "text":
                temp = str(block.value)
                temp = re.findall(r'>(.*?)</p>', temp)[0]
                return temp
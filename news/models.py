from django.db import models
from django.db.models.expressions import F
import re

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

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
        features=['underline', 'bold', 'italic', 'blockquote', 'hr', 'link']
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
            features=['underline', 'bold', 'italic', 'hr', 'link'])
        ),
        ('news_item', NewsItem(icon='edit'))
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('images'),
        StreamFieldPanel('body')  
    ]

    def first_paragraph(self):
        for block in self.body:
            if block.block_type == "text":
                temp = str(block.value)
                temp = re.findall(r'>(.*?)</p>', temp)[0]
                return temp + " <em>[…]</em>"
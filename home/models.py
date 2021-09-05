from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    max_count = 1

    home_page_text = RichTextField(
        blank=True,
        features=['h1', 'h2', 'bold', 'italic', 'image', 'link', 'hr', 'lede']
        )
    
    content_panels = Page.content_panels + [
        FieldPanel("home_page_text")
    ]


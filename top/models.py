from django.db import models
# from datetime import datetime


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

    # def __str__(self):
    #     date = self.updated.strftime('%a, %-d %b %Y')
    #     return date
from django.contrib.syndication.views import Feed
from news.models import NewsPage
from django.utils.feedgenerator import Atom1Feed

class RssFeed(Feed):
    title = "Mozart: New Documents"
    link = "https://mozartdocuments.herokuapp.com"
    description = "Announcements from Mozart: New Documents"
    feed_url = 'https://mozartdocuments.herokuapp.com/rss'
    author_name = 'Dexter Edge'
    categories = ("mozart", "musicology", "18th-century", "music history")

    language = 'en'

    def items(self):
        return NewsPage.objects.order_by('-date')[:5]

    def item_title(self, item):
        return item.title

    # return a short description of article
    def item_description(self, item):
        return item.first_paragraph()

    # return the URL of the article
    def item_link(self, item):
        return item.url

    # return the date the article was published
    def item_pubdate(self, item):
        return item.first_published_at

    # return the date of the last update of the article
    def item_updateddate(self, item):
        return item.last_published_at

class AtomFeed(RssFeed):
    feed_type = Atom1Feed
    link = "https://mozartdocuments.herokuapp.com/atom/"
    subtitle = RssFeed.description
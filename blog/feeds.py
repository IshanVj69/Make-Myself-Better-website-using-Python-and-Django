from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Bost

class LatestBostFeed(Feed):
    title = 'Make Myself Better'
    link = reverse_lazy('blog:post_list')
    description = 'New Post of my Blog'

    def items(self):
        return Bost.published.all()[:5]


    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)
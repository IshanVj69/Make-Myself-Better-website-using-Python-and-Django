from django.contrib.sitemaps import Sitemap
from .models import Bost


class BostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Bost.published.all()

    def lastmod(self, obj):
        return obj.updated

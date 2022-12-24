"""Motivate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BostSitemap
from django.conf import settings  # add this
from django.conf.urls.static import static  # add this

# urlpatterns = [
# path('admin/', admin.site.urls),
# path('', views.index, name='index'),
# ]

sitemaps = {'posts': BostSitemap, }

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('app2.urls')),
                  path('admin/', admin.site.urls),
                  path('app3/', include('app3.urls')),
                  path('app4/', include('app4.urls')),
                  path('app5/', include('app5.urls')),
                  path('app7/', include('app7.urls')),
                  path('app8/', include('app8.urls')),
                  path('app9/', include('app9.urls')),
                  path('mailsender/', include('mailsender.urls')),
                  path('Myapp/', include('Myapp.urls')),
                  path('Article/', include('Article.urls')),
                  path('blog/', include('blog.urls', namespace='blog')),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.'),
                  path(r'comments/', include('django_comments_xtd.urls')),


                  # path('login', include('app2.urls'), name='webpage2'),
                  # path('registration', include('app2.urls'), name='webpage3'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


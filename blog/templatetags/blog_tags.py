from django import template
from ..models import Bost
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    return Bost.published.count()


@register.simple_tag
def get_most_commented_posts(count=5):
    return Bost.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Bost.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

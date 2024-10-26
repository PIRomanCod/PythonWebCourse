from django import template
from django.db.models import Count

from ..models import Tag

register = template.Library()


def tags(quote_tags):
    return ', '.join([str(name) for name in quote_tags.all()])


def tag(quote_tags):
    return [name for name in quote_tags.all()]


def toptags(request):
    return Tag.objects.annotate(num_quotes=Count('quote')).order_by('-num_quotes')[:10]


register.filter('tags', tags)
register.filter('tag', tag)
register.filter('toptags', toptags)
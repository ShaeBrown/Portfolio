from projects.models import Tag
from django import template

register = template.Library()


@register.inclusion_tag('top_tags.html')
def topTags():
    tags = list(Tag.objects.all())
    t = sorted(tags, key=Tag.count)
    t.reverse()
    return {'tags': t[:3]}

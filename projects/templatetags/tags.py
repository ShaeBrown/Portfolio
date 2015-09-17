from projects.models import Tag
from django import template

register = template.Library()


@register.inclusion_tag('top_tags.html')
def topTags():
    tags = list(Tag.objects.all())
    t = sorted(tags, key=Tag.count)
    t.reverse()
    return {'tags': t[:3]}

@register.inclusion_tag('project.html')
def projects(p):
    return {'p' : p }

@register.inclusion_tag('codegroup.html')
def codegroups(g, collapse):
    return {'g': g, 'collapse' : collapse}

@register.inclusion_tag('pagination.html')
def pagination(p):
    return {'p': p }
from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project, codeGroup, code


def featured(request):
    p = Project.objects.filter(featured=True)
    g = codeGroup.objects.filter(featured=True)
    return render(request, '../templates/project.html', {'p': p, 'g': g})


def tag(request, slug):
    p = Project.objects.filter(tags__name=slug).distinct()
    g = codeGroup.objects.filter(code__tags__name = slug).distinct()
    for group in g:
        group.c = code.objects.filter(tags__name = slug, group__id = group.id)
    return render(request, '../templates/tags.html', {'p': p, 'g': g})
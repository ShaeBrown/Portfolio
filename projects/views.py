
from django.shortcuts import render
from django.db.models import Q
from projects.models import Project, codeGroup, code, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def featured(request):
    p = Project.objects.filter(featured=True).order_by('-date')
    g = codeGroup.objects.filter(featured=True)
    return render(request, '../templates/featured.html', {'p': p, 'g': g})


def all(request):
    p = Project.objects.all().order_by('-date')
    g = codeGroup.objects.all()
    paginator = Paginator(p, 5)
    page = request.GET.get('page')
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        p = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        p = paginator.page(paginator.num_pages)
    return render(request, '../templates/all.html', {'p': p, 'g': g})

def tag(request, slug):
    tag = Tag.objects.filter(id=slug).distinct()
    p = Project.objects.filter(tags__id=slug).distinct().order_by('-date')
    g = codeGroup.objects.filter(code__tags__id=slug).distinct()
    for group in g:
        group.c = code.objects.filter(tags__id=slug, group__id=group.id)
    paginator = Paginator(p, 5)
    page = request.GET.get('page')
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        p = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        p = paginator.page(paginator.num_pages)
    return render(request, '../templates/tags.html', {'tag': tag, 'p': p, 'g': g})


def search(request):
    query = request.GET.get('input').split()

    if query:

        pset = Q()
        gset = Q()
        cset = Q()
        codeset = Q()

        for term in query:

            pset |= Q(name__contains=term)
            pset |= Q(info__contains=term)
            pset |= Q(description__contains=term)
            pset |= Q(tags__id__contains=term)

            gset |= Q(name__contains=term)
            gset |= Q(info__contains=term)

            cset |= Q(code__tags__id__contains=term)
            cset |= Q(code__description__contains=term)
            cset |= Q(code__name__contains=term)

            codeset |= Q(tags__id__contains=term)
            codeset |= Q(description__contains=term)
            codeset |= Q(name__contains=term)

        c = codeGroup.objects.filter(cset).distinct()
        p = Project.objects.filter(pset).distinct().order_by('-date')
        g = codeGroup.objects.filter(gset).distinct()

        for group in g:
            group.c = group.codes()

        for group in c:
            group.c = group.codes().filter(codeset)

        g = list(g)
        c = list(c)

        g = g + list(set(c) - set(g))

    else:

        p = Project.objects.all()
        g = codeGroup.objects.all()

    return render(request, '../templates/search.html', {'query': query, 'p': p, 'g': g})

from django.shortcuts import render, HttpResponseRedirect
from projects.models import Project, codeGroup, code, Tag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from projects.filters import ProjectFilter, CodeFilter
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def featured(request):
    p = Project.objects.filter(featured=True)
    p = ProjectFilter(request.GET, queryset=p)
    g = codeGroup.objects.filter(featured=True)
    g = CodeFilter(request.GET, queryset=g)
    for group in g:
        group.c = group.codes()
    return render(request, '../templates/portfolio.html', {'msg' : 'viewing featured..', 'collapse' : 1, 'p': p, 'g': g})


def contact(request):
    subject = "Contact from shaebrown.me"
    from_email = request.GET.get('email')
    phone = request.GET.get('phone')
    message = request.GET.get('message')

    if phone and message and from_email:
        message = "From: " + str(from_email) + "\nPhone: " + str(phone) + "\n" + message
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['shaeamandabrown@gmail.com'], fail_silently=False)
            messages.success(request, "Email sent successfully", extra_tags="alert alert-success")
        except Exception as e:
            messages.error(request, "Error, email could not send" + e.__class__.__name__,
                           extra_tags="alert alert-danger")
    else:
        messages.error(request, "Error,  form or request", extra_tags="alert alert-danger")
    return HttpResponseRedirect(request.GET.get('redirect'))


def all(request):
    p = Project.objects.all()
    g = codeGroup.objects.all()

    g = CodeFilter(request.GET, queryset=g)

    for group in g:
        group.c = group.codes()

    p = ProjectFilter(request.GET, queryset=p)
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
    return render(request, '../templates/portfolio.html', {'msg' : 'viewing all..', 'collapse' : 0, 'p': p, 'g': g})

def tag(request, slug):
    tag = Tag.objects.filter(id=slug).distinct()
    p = Project.objects.filter(tags__id=slug).distinct()
    p = ProjectFilter(request.GET, queryset=p)
    g = codeGroup.objects.filter(code__tags__id=slug).distinct()

    for group in g:
        group.c = list(code.objects.filter(tags__id=slug, group__id=group.id))


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

    msg = "viewing "
    for t in tag:
        msg += t.name
    msg += "..."

    return render(request, '../templates/portfolio.html', {'msg': msg, 'collapse' : 0 , 'p': p, 'g': g})


def search(request):

    if not request.GET.get('input'):
        p = request.session['p']
        g = request.session['g']
        query = request.session['q']

    if request.GET.get('input'):

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
            p = Project.objects.filter(pset).distinct()
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

        request.session['p'] = p
        request.session['g'] = g
        request.session['q'] = query

    p = ProjectFilter(request.GET, queryset=p)

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

    msg = 'viewing search for \"'
    for q in query:
        msg += q + " "
    msg += '\"...'

    return render(request, '../templates/portfolio.html', {'msg': msg, 'collapse' : 1, 'p': p, 'g': g})

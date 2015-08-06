
from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project, Tag


def featured(request):
    p = Project.objects.filter(featured = True)
    return render(request,'../templates/project.html', {'p': p })

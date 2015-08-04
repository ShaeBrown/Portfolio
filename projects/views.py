
from django.http import HttpResponse
from django.shortcuts import render
from projects.models import Project


def index(request):
    p = Project.objects.filter(featured = True)
    return render(request,'../templates/index.html', {'p': p })
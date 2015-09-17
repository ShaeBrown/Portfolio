import django_filters
from projects.models import Project, codeGroup


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        order_by = ['-date', 'name']
        fields = []


class CodeFilter(django_filters.FilterSet):
    class Meta:
        model = codeGroup
        order_by = ['name', '-date']
        fields = []

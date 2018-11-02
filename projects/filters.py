import django_filters
from projects.models import Project, CodeGroup


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        order_by = ['-date', 'name']
        fields = []


class CodeFilter(django_filters.FilterSet):
    class Meta:
        model = CodeGroup
        order_by = ['name', '-date']
        fields = []

import django_filters
from projects.models import Project
from django.db.models.functions import Lower


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        order_by = ['name', '-date']
        fields = []

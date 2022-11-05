from django.core.exceptions import ValidationError
from django_filters import rest_framework as filters

from reviews.models import Title


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TitlesFilter(filters.FilterSet):
    genre = CharFilterInFilter(
        field_name='genre__slug', lookup_expr='in')
    category = CharFilterInFilter(
        field_name='category__slug', lookup_expr='in')

    class Meta:
        model = Title
        fields = ['name', 'year', 'genre', 'category']

import django_filters
from .models import FoodProducts
from django.db.models import Q, F

class FoodProductsFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name="product", lookup_expr='icontains')
    ingredients = django_filters.CharFilter(field_name="ingredients", lookup_expr='icontains')
    #allergens = django_filters.CharFilter(field_name="allergens", lookup_expr='icontains')
    calories = django_filters.NumberFilter()
    calories__gt = django_filters.NumberFilter(field_name='calories', lookup_expr='gt')
    calories__lt = django_filters.NumberFilter(field_name='calories', lookup_expr='lt')
    country = django_filters.CharFilter(field_name="country", lookup_expr='iexact')
    store = django_filters.CharFilter(field_name="store", lookup_expr='iexact')
    glutenfree = django_filters.BooleanFilter(field_name="glutenfree")
    vegan = django_filters.BooleanFilter(field_name="vegan")
    vegetarian = django_filters.BooleanFilter(method='vegetarian_filter')
    #halal = django_filters.BooleanFilter(method='halal_filter')
    halal = django_filters.BooleanFilter(field_name="halal")
    #kosher = django_filters.BooleanFilter(method='kosher_filter')
    kosher = django_filters.BooleanFilter(field_name="kosher")
    sugarfree = django_filters.BooleanFilter(method='sugarfree_filter')

    class Meta:
        model = FoodProducts
        fields = ['product', 'ingredients', 'calories', 'country', 'store', 'glutenfree', 'vegan', 'vegetarian', 'halal', 'kosher']

    def vegetarian_filter(self, queryset, name, value):
        return queryset.filter(Q(vegetarian__iexact = 'True') | Q(vegan__iexact = 'True'))

    '''
    def halal_filter(self, queryset, name, value):
        return queryset.filter(Q(halal__iexact = 'True') | Q(vegetarian__iexact = 'True') | Q(vegan__iexact = 'True'))

    def kosher_filter(self, queryset, name, value):
        return queryset.filter(Q(kosher__iexact = 'True') | Q(vegetarian__iexact = 'True') | Q(vegan__iexact = 'True'))
    	
    def sugarfree_filter(self, queryset, name, value):
        return queryset.filter(Q(ingredient__icontains = F('sugar')) | Q(ingredient__icontains = F('Sugar')))
    '''

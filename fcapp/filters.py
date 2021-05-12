import django_filters
from .models import FoodProducts
from django.db.models import Q

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
    halal = django_filters.BooleanFilter(method='halal_filter')
    kosher = django_filters.BooleanFilter(method='kosher_filter')

    class Meta:
        model = FoodProducts
        fields = ['product', 'ingredients', 'calories', 'country', 'store', 'glutenfree', 'vegan', 'vegetarian', 'halal', 'kosher']

    def vegetarian_filter(self, queryset, name, value):
        return queryset.filter(Q(vegetarian__iexact = 'True') | Q(vegan__iexact = 'True'))

    def halal_filter(self, queryset, name, value):
        return queryset.filter(Q(halal__iexact = 'True') | Q(vegetarian__iexact = 'True') | Q(vegan__iexact = 'True'))

    def kosher_filter(self, queryset, name, value):
        return queryset.filter(Q(kosher__iexact = 'True') | Q(vegetarian__iexact = 'True') | Q(vegan__iexact = 'True'))

    '''
	# 1. query all items form foodproducts where country = 'United States'
	country = FoodProducts.objects.filter(country__iexact = 'United States')

	# 2. all the ones from Wholefoods
	store = FoodProducts.objects.filter(store__iexact = 'Wholefoods')

	# 3. all the ones with less than 300 calories
	calories = FoodProducts.objects.filter(calories__lt = 300)

	# 4. all the ones listed as Vegan
	vegan = FoodProducts.objects.filter(vegan__iexact = 'True')

	# 5. all the ones Vegetarian
	vegetarian = FoodProducts.objects.filter(Q(vegan__iexact = 'True') | Q(vegetarian__iexact = 'True'))

	# 6. all the ones Halal
	halal = FoodProducts.objects.filter(Q(vegan__iexact = 'True') | Q(vegetarian__iexact = 'True') | Q(halal__iexact = 'True'))
	
	# 7. all the ones Kosher
	kosher = FoodProducts.objects.filter(Q(vegan__iexact = 'True') | Q(vegetarian__iexact = 'True') | Q(kosher__iexact = 'True'))

	# 8. all the ones Gluten-free
	glutenfree = FoodProducts.objects.filter(glutenfree = 'True')

	# testing a really weird one
	#weird = FoodProducts.objects.filter(Q(vegan__iexact = 'True') | Q(vegetarian__iexact = 'True')).filter(calories__lt = 175)
    '''
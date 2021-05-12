from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.core import serializers
from django.core.paginator import Paginator
from .models import FoodProducts
from .filters import FoodProductsFilter
from .forms import CustomUserChangeForm, RegisterForm
import json

# Create your views here.

def index(response):
	'''
	products = FoodProducts.objects.all()
	filter = FoodProductsFilter(response.GET, queryset=products)
	products = filter.qs
	'''

	return render(response, 'home.html')

def table(response):
    products = FoodProducts.objects.order_by('product')
	
    filter = FoodProductsFilter(response.GET, queryset=products)	
    filtered_data = serializers.serialize('python', filter.qs)
    processed_filtered_data = [d['fields'] for d in filtered_data]
    totalproducts = len(processed_filtered_data)

    page = response.GET.get('page')
    paginator = Paginator(processed_filtered_data, 50)
    paginated_data = paginator.page(page)

    #raw_data = serializers.serialize('python', filter.qs)
    #actual_data = [d['fields'] for d in raw_data]
    #raw_data = serializers.serialize('python', paginated_data)
    
    json_products = {
		'total_products': totalproducts,
		'products': list(paginated_data)
	}
    #json_products = { 'total_products': totalproducts, 'data': list(paginated_data) }

    return HttpResponse(json.dumps(json_products), content_type="application/json")

def register(response):
	if response.method == 'POST':
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = RegisterForm()

	return render(response, 'registration/register.html', {'form': form})

def savesettings(response):
    message = 'User not updated; form invalid'
    if response.method == 'POST' and response.user.is_authenticated:

        #data = json.loads(response.body)
        form = CustomUserChangeForm(data=response.POST,instance=response.user)
        if form.is_valid():
            form.save()
            message = 'Valid form; updated user'
        return HttpResponse({"message":message}, content_type="application/json", status=201)
    else:
        return HttpResponse({"message":message}, content_type="application/json", status=400)

'''
def product(response, id):
	item = FoodProducts.objects.get(id=id)
	return render(response, 'product.html', { 'title': item.product, 'item': item })
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('<int:id>', views.product, name='product'),
	#path('table/', views.table, name='table'),
]
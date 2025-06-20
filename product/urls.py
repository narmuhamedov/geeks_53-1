from django.urls import path
from . import views

urlpatterns = [
  path('all_products/', views.all_products, name='all_products'),
  path('drinks_product/', views.drinks_product, name='drinks_product')
]
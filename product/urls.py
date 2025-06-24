from django.urls import path
from . import views

urlpatterns = [
  path('all_products/', views.AllProductsView.as_view(), name='all_products'),
  path('drinks_product/', views.DrinksProductView.as_view(), name='drinks_product'),
]
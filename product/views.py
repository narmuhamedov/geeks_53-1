from django.shortcuts import render
from . import models
from django.views import generic

# #all products
class AllProductsView(generic.ListView):
   model = models.Product
   template_name = 'manyTOmany/all_products.html'
   context_object_name = 'all_products'
   ordering = ['-id']


# def all_products(request):
#   if request.method == "GET":
#     all_products = models.Product.objects.all().order_by('-id')
#     context = {
#       'all_products': all_products,
#     }
#     return render(request, template_name='manyTOmany/all_products.html', context=context)

# #filter tags = Напитки
class DrinksProductView(generic.View):
   def get(self, request):
      drinks_product = models.Product.objects.filter(tags__name='#Напитки').order_by('-id')
      context = {
         'drinks_product': drinks_product,
      }
      return render(request, template_name='manyTOmany/drinks_product.html', context=context)
      



# def drinks_product(request):
#     if request.method == "GET":
#      drinks_product = models.Product.objects.filter(tags__name='#Напитки').order_by('-id')
#      context = {
#         'drinks_product': drinks_product,
#      }
#     return render(request, template_name='manyTOmany/drinks_product.html', context=context)
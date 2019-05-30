from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render, redirect, reverse
from rainforest.models import Product
from django.views.decorators.http import require_http_methods


def root(request):
  return redirect('products_list')

def products_page(request):
  context = {
    'title': 'Products',
    'products': Product.objects.all()
  }
  
  response = render(request, 'index.html', context)
  return HttpResponse(response)

def product_details(request, id):
  product = Product.objects.get(pk=id)
  context = {
    'title': product.name,
    'product': product,
  }
  response = render(request, 'product.html', context)
  return HttpResponse(response)
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render, redirect, reverse
from rainforest.models import Product
from django.views.decorators.http import require_http_methods


def root(request):
  return HttpResponseRedirect('/products')

def products_page(request):
  context = {
    'title': 'Products',
    'products': Product.objects.all()
  }
  
  response = render(request, 'index.html', context)
  return HttpResponse(response)

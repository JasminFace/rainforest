from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render, redirect, reverse
from rainforest.models import Product
from django.views.decorators.http import require_http_methods
from rainforest.forms import ProductForm


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


def product_new(request):
  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      product = form.save()
      product.save()
      return redirect('product_details', id=product.id)
  else:
    form = ProductForm()
  context = {
    'form': form,
  }
  return render(request, 'newproduct.html', context)


def product_edit(request, id):
  product = Product.objects.get(pk=id)
  form = ProductForm(instance=product)
  context = {
    'form': form,
    'title': 'Product Edit',
    'product': product,
  }
  response = render(request, 'edit.html', context)
  return HttpResponse(response)

def edit_submit(request, id):
  if request.method == 'POST':
    product = Product.objects.get(pk=id)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
      save_product = form.save()
      save_product.save()
      return redirect('product_details', id=product.id)
  else:
    form = ProductForm()
  context = {
    'form': form,
    'product': product,
  }
  return render(request, 'product_edit', context)


def delete_product(request, id):
  product = Product.objects.get(pk=id)
  product.delete()
  return redirect('products_list')
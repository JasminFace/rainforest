from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from django.shortcuts import render, redirect, reverse
from rainforest.models import Product, Review
from django.views.decorators.http import require_http_methods
from rainforest.forms import ProductForm, ReviewForm


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
  form = ReviewForm()
  context = {
    'title': product.name,
    'product': product,
    'form': form,
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

def review_new(request, id):
  if request.method == 'POST':
    product = Product.objects.get(pk=id)
    form = ReviewForm(request.POST)
    if form.is_valid():
      review = form.instance
      review.product = product
      review.save()
      return redirect('product_details', id=product.id)

def edit_review(request, id):
  review = Review.objects.get(pk=id)
  form = ReviewForm(instance=review)
  context = {
    'form': form,
    'title': 'Review Edit',
    'review': review
  }
  response = render(request, 'review_edit.html', context)
  return HttpResponse(response)

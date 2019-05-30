from django import forms
from rainforest.models import Product

class ProductForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = ('name', 'description', 'price_in_cents')
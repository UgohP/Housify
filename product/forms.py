# from pyexpat import model
from django import forms
from .models import Product

# from product.models import Customer
class ProductForm(forms.ModelForm):
    """A class form for the product"""
    
    class Meta:
        model = Product
        exclude = ['slug', 'created_by']
from django.shortcuts import render
import random
from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.views.generic.edit import *
from core.models import Categorie

# Create your views here.

# def product(request, prod):
#     context = {}
    
#     return render(request, 'product.html', context)

def product(request, pk):
    category = Categorie.objects.get(category_name=pk)
    product = Product.objects.filter(category=category)
    context = {'product':product}
    
    return render(request, 'fashion.html', context)

def getProduct(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product':product}

    return render(request, 'get_product.html', context) 



def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user.vendor

            product.save()   
            messages.success(request, str(product.product_name) + ' was created Successfully!!')
            return redirect('history')
    else:
        form = ProductForm()
    context = {'form':form}
    return render(request, 'create_product.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully!!')
            return redirect('history')
    context = {'form':form}
    return render(request, 'update_product.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
def deleteProduct(request, pk):

    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Deleted Successfully!!')
        return redirect('history')
    context = {'product': product}
    return render(request, 'delete_product.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['vendor'])
def history(request):
    vendor = request.user.vendor
    product = Product.objects.filter(created_by=vendor)

    context = {'product':product}
    return render(request, 'history.html', context)

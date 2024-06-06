from django.shortcuts import render
from .models import Carousel, Categorie
from product.models import Product

# Create your views here.
def homepage(request):
    """view for homepage"""
    
    carousel = Carousel.objects.all()
    category = Categorie.objects.all()
    product = Product.objects.all()
    
    context = {'carousel':carousel, 'category':category, 'product':product}
    return render(request, 'homepage.html', context)


# @login_required(login_url='login')
def categories(request):
    """"View for categories"""

    context = {}
    return render(request, 'categories.html', context)

from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def product_individual(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'products':product})
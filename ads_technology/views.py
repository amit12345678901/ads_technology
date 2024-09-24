from django.shortcuts import render, get_object_or_404
from .models import Carausel, Category,Product

def home(request):
    obj = Carausel.objects.all()  # Fetch all carousel objects
    context = {
        'obj': obj  # Pass the fetched objects to the template
    }
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def home1(request):
    obj = Category.objects.all()  # Fetch all categories
    products = Product.objects.all()  # Fetch all products
    context = {
        'categories': obj,
        'products': products
    }
    return render(request, 'home2.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category_detail.html', {'category': category})

def product_list(request):
    products = Product.objects.all()  # Fetch all products
    print(products)
    return render(request, 'product_list.html', {'products': products})
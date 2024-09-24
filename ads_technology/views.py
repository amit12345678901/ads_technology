from django.shortcuts import render, get_object_or_404
from .models import Carausel, Category

def home(request):
    obj = Carausel.objects.all()  # Fetch all carousel objects
    context = {
        'obj': obj  # Pass the fetched objects to the template
    }
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def home1(request):
    # return render(request, 'your_template.html', )
    obj = Category.objects.all()
    return render(request, 'home2.html', {'categories': obj})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category_detail.html', {'category': category})

from django.shortcuts import render
from .models import Carausel

def home(request):
    obj = Carausel.objects.all()  # Fetch all carousel objects
    context = {
        'obj': obj  # Pass the fetched objects to the template
    }
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def home1(request):
    return render(request, 'home2.html')


from django.shortcuts import render
from .models import Carausel

def home(request):
    obj = Carausel.objects.all()  # Fetch all carousel objects
    context = {
        'obj': obj  # Pass the fetched objects to the template
    }
    return render(request, 'home.html', context)

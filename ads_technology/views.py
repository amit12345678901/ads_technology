from django.shortcuts import render, get_object_or_404
from .models import Carausel, Category,Product,Contact
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
# from .forms import ContactForm
# from .models import ContactForm
def home(request):
    obj = Category.objects.all()  # Fetch all categories
    products = Product.objects.all()  # Fetch all products
    context = {
        'categories': obj,
        'products': products
    }
    return render(request, 'home2.html', context)

def login(request):
    return render(request, 'login.html')

# def home1(request):
    

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category_detail.html', {'category': category})

def product_list(request):
    products = Product.objects.all()  # Fetch all products
    print(products)
    return render(request, 'product_list.html', {'products': products})

# contact form

# def contact_view(request):
#     if request.method == 'POST':
#         form = Contact(request.POST)  # Create an instance of ContactForm with POST data
#         if form.is_valid():  # Check if the form is valid
#             # Create a Contact instance with cleaned data
#             contact = Contact(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 phone=form.cleaned_data['phone'],
#             )
#             contact.clean()  # Validate the contact instance using the clean method
#             contact.save()  # Save the contact instance to the database
#             return redirect('success')  # Redirect to a success page (ensure this URL is defined in your urls.py)
#     else:
#         form = ContactForm()  # Create a blank form for GET requests

#     return render(request, 'contact.html', {'form': form})  # Render the contact page with the form

def contact_view(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # You can add any additional validations here
        if not name or not email or not phone:
            return JsonResponse({"errors": "All fields are required."}, status=400)

        try:
            contact.name = name
            contact.email = email
            contact.phone = phone
            contact.save()
            return JsonResponse({"message": "Save successful!"})
        except Exception as e:
            # Log the exception if needed
            return JsonResponse({"errors": str(e)}, status=400)

    return render(request, 'home2.html')

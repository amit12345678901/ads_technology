"""
URL configuration for ads_technology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ads_technology import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),  # Added trailing slash for consistency
    # path('home2/', views.home1, name='home2'),  # Added trailing slash for consistency
    # path('categories/', views.category_list, name='category_list'),  # Uncomment if you want this route
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('contact/', views.contact_view, name='contact'),
]

# Add media URL patterns for serving uploaded media files
if settings.DEBUG:  # Only serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

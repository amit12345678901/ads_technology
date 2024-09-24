from django.db import models
from django.utils.text import slugify
from django import forms
import re

# Models
class Carausel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='pics/%Y/%m/%d/')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories/')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    dec = models.CharField(max_length=150, verbose_name="Description")

    def __str__(self):
        return f"{self.name}: {self.dec}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/category/{self.slug}/"

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    review_count = models.PositiveIntegerField()
    discount_percentage = models.PositiveIntegerField()
    rating = models.FloatField()  # Rating out of 5

    def __str__(self):
        return self.title

# Form Definition (inside models.py)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.email})"

    def clean(self):
        # Validate phone number format before saving to the database
        phone = self.phone
        if not re.match(r'^\+?\d{7,15}$', phone):
            raise ValidationError("Enter a valid phone number with 7-15 digits.")
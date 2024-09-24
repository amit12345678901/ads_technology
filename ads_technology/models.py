from django.db import models
from django.utils.text import slugify
from django.utils.text import slugify  # Import slugify

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
        return f"{self.name}: {self.dec}"  # Return both name and description

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f"/category/{self.slug}/"


# ads_technology/models.py
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


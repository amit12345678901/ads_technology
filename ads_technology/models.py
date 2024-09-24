from django.db import models

class Carausel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='pics/%Y/%m/%d/')

    def __str__(self):
        return self.title

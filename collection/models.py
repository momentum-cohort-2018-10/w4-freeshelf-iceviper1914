from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    # image = models.ImageField(upload_to='initial_data/')
    brand = models.CharField(max_length=255)
    # slug = models.SlugField(unique=True)
# Create your models here.

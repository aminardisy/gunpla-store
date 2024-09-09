from django.db import models

class Gunpla(models.Model):
    name =  models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(default='No description available')
    size_ratio = models.CharField(max_length=10)
    extensions = models.CharField(max_length=255)
    notes = models.TextField()

# Create your models here.

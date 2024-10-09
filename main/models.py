import uuid
from django.db import models
from django.contrib.auth.models import User

class Gunpla(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name =  models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(default='No description available')
    size_ratio = models.CharField(max_length=10)
    extensions = models.CharField(max_length=255, default="No extansions available")
    notes = models.TextField(default='No notes available')

# Create your models here.

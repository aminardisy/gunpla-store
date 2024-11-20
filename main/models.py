import uuid
from django.db import models
from django.contrib.auth.models import User

class Gunpla(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name =  models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(default=None)
    size_ratio = models.CharField(max_length=10)
    extensions = models.CharField(max_length=255, default=None)
    notes = models.TextField(default=None)

# # project id (uuid), name (chara max 255)
# # emplyi dapartement(chara max 100), projects (satu project bisa ke banyak emplyi dan sebaliknya), user

# class Project(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=255)

# class Employee(models.Model):
#     departement = models.CharField(max_length=100)
#     projects = models.ManyToManyField(Project)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# Create your models here.

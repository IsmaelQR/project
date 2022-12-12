from django.db import models

# Create your models here.
class User(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Project(models.Model):
    # id = models.AutoField(primary_key=True)
    photo = models.CharField(max_length=1000)
    title= models.CharField(max_length=50)
    tags= models.CharField(max_length=50)
    description= models.CharField(max_length=1000)
    git= models.CharField(max_length=50)
    
    
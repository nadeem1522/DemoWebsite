from django.db import models

# Create your models here.

class Team(models.Model):
    photo= models.ImageField(upload_to='photos/%Y/%m/%d')
    text=models.CharField(max_length=100,default="")
    created_date = models.DateTimeField(auto_now_add=True)
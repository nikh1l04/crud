from django.db import models

# Create your models here.



class Crud(models.Model):
    Slno=models.IntegerField()
    Itemname=models.CharField(max_length=255)
    Description=models.TextField()
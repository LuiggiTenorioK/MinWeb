from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    state = models.IntegerField()
    description = models.CharField(max_length=300)
    img_path = models.CharField(max_length=300)
    #img_path = models.FilePathField(path = '/static/img/',recursive=True)

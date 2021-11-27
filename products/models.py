from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField( max_length=50)
    percentage = models.IntegerField()

class Products(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    sellin_price = models.IntegerField()
    quantity = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredients)


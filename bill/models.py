from django.db import models
from django.db.models.fields import FloatField

# Create your models here.


class Bill(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    user_id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.IntegerField()

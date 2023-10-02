from django.db import models

# Create your models here.


class Orders(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0, null=True)
    description = models.CharField(default='', max_length=100)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Member(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return self.name


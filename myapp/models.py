from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0, null=True)
    description = models.CharField(max_length=100, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    def __str__(self):
        return self.name
    
    

class Member(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(default='+880', max_length=14, null=True)

    def __str__(self):
        return self.name


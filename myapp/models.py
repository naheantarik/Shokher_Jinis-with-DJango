from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0, null=True)
    description = models.CharField(default='', max_length=100)
    image = models.ImageField('media/product')
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


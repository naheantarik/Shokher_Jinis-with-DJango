from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    product = Product.get_all_product()

    return render(request, 'dashboard.html', {'products': product})
from django.shortcuts import render
from django.utils import timezone

from .models import Products
from .models import Cateogory
from .models import SubCateogory
# Create your views here.

def index(request):
    products = Products.objects.all()
    categories = Cateogory.objects.all()
    subCategories = SubCateogory.objects.all()
    return render(request, 'index.html',{'products': products, 'categories': categories, 'subCategories': subCategories})
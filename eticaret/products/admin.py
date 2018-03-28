from django.contrib import admin

# Register your models here.
from products.models import Products
from products.models import Cateogory
from products.models import SubCateogory

class productsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Products,productsAdmin)
admin.site.register(Cateogory,productsAdmin)
admin.site.register(SubCateogory,productsAdmin)
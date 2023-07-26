from django.contrib import admin
from .models import Product,ImageProduct

# Register your models here.

 
admin.site.register(ImageProduct)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("name","reference","quantity","store","price",)
    
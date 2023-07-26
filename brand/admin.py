from django.contrib import admin
from .models import Brand

# Register your models here.


@admin.register(Brand)
class BrandAmin(admin.ModelAdmin):
    
    list_display=("name","code")
    list_filter=("name",)

     

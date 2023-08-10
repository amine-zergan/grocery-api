from django.contrib import admin
from .models import Category
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display=('name','background',"image",)
    list_filter=("name",)
from django.contrib import admin
from .models import Category
from import_export.admin import ImportExportModelAdmin
from .form import CategoryForm
# Register your models here.
#admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    form=CategoryForm
    list_display=('name','background',"image",)
    list_filter=("name",)
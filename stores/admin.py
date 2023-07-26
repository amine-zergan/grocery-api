from django.contrib import admin
from .models import Store
# Register your models here.

 

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display=("title","address","heur_ouverture","heur_fermeture","disponibilé","jour_repos")
    list_filter=("zone","rgion",)
    list_per_page=10
    date_hierarchy="created"
    search_fields=("title__startswith",)
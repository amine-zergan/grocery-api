from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from rest_framework.decorators import action
from .serializers import ProductSerialize
from rest_framework import filters

# Create your views here.APVIew flask Rest-x Response 
class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerialize
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category',"brand"]
    # /products/?search=params=> return list<Product>

    @action(detail=True, methods=['post'])
    def get_product(self, request, pk=None):
        pass



# Create your views here.

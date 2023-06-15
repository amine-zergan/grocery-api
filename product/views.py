from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerialize

# Create your views here.
class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerialize
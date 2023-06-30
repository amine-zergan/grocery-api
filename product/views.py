from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from rest_framework.decorators import action
from .serializers import ProductSerialize

# Create your views here.
class ProductView(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerialize


    @action(detail=True, methods=['post'])
    def get_product(self, request, pk=None):
        pass



# Create your views here.

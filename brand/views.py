from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import BrandSerializer
from .models import Brand

# Create your views here.


class BrandView(ModelViewSet):
    queryset=Brand.objects.all()
    serializer_class=BrandSerializer
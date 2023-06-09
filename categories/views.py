from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Category
from .serializers import CategorieSerialize



class CategorieView(ModelViewSet):
    """
    A viewset for viewing and editing Category instances.
    """
    queryset=Category.objects.all()
    serializer_class=CategorieSerialize
    permission_classes=[AllowAny]

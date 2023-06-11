from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Store
from .serializers import StoreSerialize



class StoreView(ModelViewSet):
    """
    A viewset for viewing and editing Category instances.
    """
    queryset=Store.objects.all()
    serializer_class=StoreSerialize
    permission_classes=[AllowAny]
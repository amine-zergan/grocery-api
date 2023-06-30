from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import PromotionsSerialize
from .models import Promotions


# Create your views here.


class PromotionsView(ModelViewSet):
    serializer_class=PromotionsSerialize
    queryset=Promotions.objects.all()


    
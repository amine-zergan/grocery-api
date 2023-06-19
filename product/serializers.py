from rest_framework import serializers
from .models import Product, ImageProduct
from stores.serializers import StoreSerialize
from categories.serializers import CategorieSerialize



class ImageProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=ImageProduct
        fields="__all__"

class ProductSerialize(serializers.ModelSerializer):
    category=CategorieSerialize( )
    store=StoreSerialize()
    images = ImageProductSerialize(many=True)
    class Meta:
        model=Product
        fields=["name","reference","weigth","price","units","description","quantity","store","category","images"]
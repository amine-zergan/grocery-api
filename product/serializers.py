from rest_framework import serializers
from .models import Product, ImageProduct
from categories.serializers import CategorieSerialize



class ImageProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=ImageProduct
        fiels="__all__"

class ProductSerialize(serializers.ModelSerializer):
    category=CategorieSerialize()
    image=ImageProductSerialize()
    class Meta:
        model=Product

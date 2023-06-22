from rest_framework import serializers
from .models import Category
from product.serializers import ProductSerialize

class CategorieSerialize(serializers.ModelSerializer):
    products=ProductSerialize(many=True)
    class Meta:
        model=Category
        fields = ['id', 'name', 'create_at','background','image','products']
        
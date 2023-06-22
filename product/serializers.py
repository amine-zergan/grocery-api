from rest_framework import serializers
from .models import Product, ImageProduct
 



class ImageProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=ImageProduct
        fields=['id','image']

class ProductSerialize(serializers.ModelSerializer):
    #category=CategorieSerialize( )
    #store=StoreSerialize()
    images = ImageProductSerialize(many=True)
    class Meta:
        model=Product
        fields=["name","reference","weigth","price","units","description","quantity","images"]
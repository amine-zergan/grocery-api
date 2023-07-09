from rest_framework import serializers
from .models import Product, ImageProduct
from brand.serializer import BrandSerializer
 



class ImageProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=ImageProduct
        fields=['id','image']

class ProductSerialize(serializers.ModelSerializer):
    #category=CategorieSerialize( )
    #store=StoreSerialize()
    images = ImageProductSerialize(many=True)
    brands=serializers.StringRelatedField(read_only=False)
    class Meta:
        model=Product
        fields=["id","name","reference","weigth","price","units","description","quantity","images","brands"]
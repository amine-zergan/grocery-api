from rest_framework import serializers
from .models import Category

class CategorieSerialize(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['id', 'name', 'created']
        
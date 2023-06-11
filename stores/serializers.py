
from rest_framework import serializers
from .models import Store

class StoreSerialize(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'
 
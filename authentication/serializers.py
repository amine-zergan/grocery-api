from rest_framework import serializers,validators
from django.contrib.auth.models import User



class SingUpSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=180)
    username=serializers.CharField(max_length=45)
    password= serializers.CharField(min_length=8,write_only=True)
    class Meta:
        model=User

    def validate(self, attrs):
        email_exist =User.objects.filter(email=attrs['email']).exists()
        if email_exist:
            raise validators.ValidationError("email deja exist ")
        return super().validate(attrs)
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# end-point : methode post [data => phone ] return Response : user created avec send otp, expire_at 
class CreateUser(ModelViewSet):
    pass 

"""
user : uid ,name, code otp, phone adress ! top 
=> profile : image, email for receive offre wela catalogue relation one-to-one 

"""

# end-point : methode post [data=> code ,uid user  ] :
# if uid exist : user created with phone .=> start testing :
#        if user.code == code and expire_at< deltaTime(second=30) ok 200 
#           if not ok : 
#             decrement number_essaye --
#             autre essaye : max=0 => return after 1h 
#  resend : generate code with expire_at if user.uid exist 
#   
class VerifyAccount(ModelViewSet):
    pass

class GenerateCodeOTP(ModelViewSet):
    pass
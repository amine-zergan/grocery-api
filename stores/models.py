from django.db import models


# Create your models here.
"""
store : 
    * location gps position 
    * product : ref-name-quantity-price -unit - disponible - offre -category-storeid-images -description
    * category : ref - name-images-background-storeid-
    * vente -recette : order -itemorder -itemproduct
    * employes : profile-store-post 
    * ouverture-fermeture
    * gerant 
    * contacts
"""
choice_jour=(('L',"lundi"),('M','mardi'),('Me',"mercredi"),('J',"jeudi"),("V","vendredi"),("D","samedi"),("D","dimanche"))

class Store(models.Model):
    title=models.CharField(max_length=150)
    disponibilé = models.BooleanField(default=True)
    address=models.CharField(max_length=255)
    zone=models.CharField(max_length=100)
    rgion=models.CharField(max_length=100)
    lon = models.FloatField()
    lat = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    heur_ouverture=models.CharField(max_length=5,default="08.00",)
    heur_fermeture=models.CharField(max_length=5,default="20.00",)
    jour_repos=models.CharField(choices=choice_jour,max_length=10)
    updated= models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    
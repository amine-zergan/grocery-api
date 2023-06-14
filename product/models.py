from django.db import models
from stores.models import Store
from categories.models import Category

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    reference=models.PositiveIntegerField()
    weigth=models.CharField(max_length=10)
    price=models.DecimalField(decimal_places=2,max_digits=6)
    units=models.CharField(max_length=50)
    description=models.TextField()
    quantity=models.IntegerField()
    store =models.ForeignKey(Store,related_name="store",on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    def __str__(self) -> str:
        return self.name
    


class ImageProduct(models.Model):
    image=models.ImageField(upload_to="product/")
    product=models.ForeignKey(Product,related_name="product",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.image.url.split("/")[-1]
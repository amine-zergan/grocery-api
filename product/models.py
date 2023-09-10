from django.db import models
from stores.models import Store
from categories.models import Category
from brand.models import Brand

# Create your models here.




class Product(models.Model):
    name=models.CharField(max_length=100)
    reference=models.PositiveIntegerField()
    weigth=models.CharField(max_length=10)
    price=models.DecimalField(decimal_places=2,max_digits=6)
    units=models.CharField(max_length=50)
    description=models.TextField()
    promotion=models.DecimalField(default=0.0,decimal_places=2,max_digits=6)
    quantity=models.IntegerField()
    brand=models.OneToOneField(Brand,related_name="brand",on_delete=models.CASCADE)
    store =models.ForeignKey(Store,related_name="store",on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name="products",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    



class ImageProduct(models.Model):
    image=models.ImageField(upload_to="product/")
    products=models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE )
    def __str__(self) -> str:
        return self.image.url.split("/")[-1]
    
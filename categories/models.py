from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True,)
    name=models.CharField(max_length=50,unique=True)
    image=models.ImageField(upload_to='uploads/')
    background=models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['create_at']

    def __str__(self) -> str:
        return self.name



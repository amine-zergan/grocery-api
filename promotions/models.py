from django.db import models

# Create your models here.


class Promotions(models.Model):
    url=models.ImageField(upload_to="promotions/")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['create_at']

    def __str__(self) -> str:
        return self.url

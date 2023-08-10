from import_export import resources
from .models import Category

class BookResource(resources.ModelResource):

    class Meta:
        model = Category
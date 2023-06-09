from .views import CategorieView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories', CategorieView, basename='categorie')
urlpatterns = router.urls
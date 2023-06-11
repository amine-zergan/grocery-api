from categories.views import CategorieView
from stores.views import StoreView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories', CategorieView, basename='categorie')
router.register(r'stories', StoreView, basename='stories')
urlpatterns = router.urls
from categories.views import CategorieView
from stores.views import StoreView
from rest_framework.routers import DefaultRouter
from product.views import ProductView


router = DefaultRouter()
router.register(r'categories', CategorieView, basename='categorie')
router.register(r'stories', StoreView, basename='stories')
router.register(r'product', ProductView, basename='product')
urlpatterns = router.urls
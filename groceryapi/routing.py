from categories.views import CategorieView
from stores.views import StoreView
from rest_framework.routers import DefaultRouter
from product.views import ProductView
from promotions.views import PromotionsView


router = DefaultRouter()
router.register(r'categories', CategorieView, basename='categorie')
router.register(r'stories', StoreView, basename='stories')
router.register(r'products', ProductView, basename='product')
router.register(r'promotions', PromotionsView, basename='promotion')
urlpatterns = router.urls
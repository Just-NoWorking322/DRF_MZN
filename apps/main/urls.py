from rest_framework.routers import DefaultRouter
from apps.main.views import ProductMixins, CharacteristicViewSet

router = DefaultRouter()

router.register(r'products', ProductMixins, basename='product')
router.register(r'characteristics', CharacteristicViewSet)

urlpatterns = router.urls

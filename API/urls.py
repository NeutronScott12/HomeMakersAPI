from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import ShopViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('shop', ShopViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
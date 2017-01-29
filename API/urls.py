from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import ShopViewSet, ProductViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register('shop', ShopViewSet)
router.register('product', ProductViewSet)
router.register('contact', ContactViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
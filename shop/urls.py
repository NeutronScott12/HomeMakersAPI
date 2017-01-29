from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ShopIndex.as_view(), name="index")
]
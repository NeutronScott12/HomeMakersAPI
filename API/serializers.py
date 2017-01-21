from rest_framework import serializers
from shop.models import Shop, Product

class ShopSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Shop
        fields = ('pk', 'category', 'created_at', 'updated_at')

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ('pk', 'shop', 'title', 'description', 'price', 'stock', 'created_at', 'updated_at', 'product_logo')
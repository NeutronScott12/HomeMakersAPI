from rest_framework import serializers
from shop.models import Shop, Product, Contact

class ShopSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Shop
        fields = ('pk', 'category', 'product_logo', 'products', 'created_at', 'updated_at')
        depth = 1

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ('pk', 'shop', 'title', 'short_description', 'long_description', 'price', 'stock', 'created_at', 'updated_at', 'product_logo')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = ('openingTimes', 'phone', 'email', 'road', 'town', 'county')
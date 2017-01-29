from django.contrib import admin
from .models import *

class ShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'updated_at']
    ordering = ['title']
    list_filter = ['updated_at', 'created_at']
    search_fields = ['title', 'category']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'price', 'stock', 'created_at', 'updated_at']
    ordering = ['title']
    list_filter = ['updated_at', 'created_at']
    search_fields = ['title', 'price', 'stock']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['openingTimes', 'phone', 'email', 'road', 'town', 'county', 'postcode']
    ordering = ['openingTimes']
    

# Register your models here.
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact, ContactAdmin)


admin.site.site_title = 'SFP Adminstration'
admin.site.site_header = 'Slough Furniture Project Adminstration'
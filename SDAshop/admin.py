from django.contrib import admin
from SDAshop.models import Brand, CarModel, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['brand_name', 'car_model']
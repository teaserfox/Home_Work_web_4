from django.contrib import admin
from catalog.models.category import Category
from catalog.models.products import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'category', 'name', 'purchase_price']
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']



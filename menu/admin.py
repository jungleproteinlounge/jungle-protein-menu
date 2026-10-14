from django.contrib import admin
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "sort_order", "active")
    list_editable = ("sort_order", "active")
    search_fields = ("name",)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price_cop", "active", "featured", "sort_order")
    list_filter = ("category", "active", "featured")
    list_editable = ("price_cop", "active", "featured", "sort_order")
    search_fields = ("name", "description")
    fields = ("category", "name", "description", "price_cop", "image", "sort_order", "active", "featured")

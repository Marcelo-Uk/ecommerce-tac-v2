from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')  # Colunas na tabela do admin
    search_fields = ('name', 'description')  # Campos para busca

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('created_at', 'status', 'user')
    search_fields = ('user__username', 'product__name')

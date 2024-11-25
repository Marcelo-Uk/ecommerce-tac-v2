from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Página inicial de produtos
    path('checkout/<int:product_id>/', views.checkout, name='checkout'),  # Página de checkout
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Adicionar ao carrinho
    path('cart/', views.cart_detail, name='cart_detail'),  # Detalhes do carrinho
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),  # Remover do carrinho
    path('checkout/', views.finalize_purchase, name='finalize_purchase'),  # Finalizar compra
    path('finalize-purchase/', views.finalize_purchase_backend, name='finalize_purchase_backend'),
]

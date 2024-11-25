from django.contrib import admin
from django.urls import path, include
from accounts.views import home  # Importe a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),  # Rota para produtos
    path('', include('products.urls')),  # Página inicial redireciona para produtos
]

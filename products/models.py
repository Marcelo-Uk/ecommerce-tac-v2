from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)  # Nome do produto
    description = models.TextField(blank=True, null=True)  # Descrição do produto
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço do produto
    stock = models.PositiveIntegerField(default=0)  # Quantidade em estoque
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    updated_at = models.DateTimeField(auto_now=True)  # Última atualização

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendente'),
        ('PAID', 'Pago'),
        ('FAILED', 'Falhou'),
    ]
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que fez o pedido
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Produto comprado
    quantity = models.PositiveIntegerField(default=1)  # Quantidade comprada
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Preço total do pedido
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')  # Status de pagamento

    def __str__(self):
        return f"Pedido #{self.id} - {self.product.name}"

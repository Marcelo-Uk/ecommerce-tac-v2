from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Order
from django.db import transaction
import random

def product_list(request):
    products = Product.objects.all()  # Busca todos os produtos
    return render(request, 'products/product_list.html', {'products': products})

def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Busca o produto ou retorna 404
    return render(request, 'products/checkout.html', {'product': product})

def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # Verifica se há estoque suficiente
        if product.stock > 0:
            # Cria o pedido
            order = Order.objects.create(
                user=request.user,
                product=product,
                quantity=1,  # Por enquanto, 1 por pedido
                total_price=product.price,
            )

            # Atualiza o estoque
            product.stock -= 1
            product.save()

            # Mensagem de sucesso
            messages.success(request, f"Compra de {product.name} realizada com sucesso!")
            return redirect('product_list')  # Redireciona para a lista de produtos
        else:
            # Mensagem de erro
            messages.error(request, "Estoque insuficiente para este produto.")
            return redirect('product_list')

    return render(request, 'products/checkout.html', {'product': product})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Inicializa o carrinho se ele ainda não existir
    cart = request.session.get('cart', {})
    
    # Adiciona o produto ao carrinho ou incrementa a quantidade
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1
        }

    # Salva o carrinho na sessão
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    return render(request, 'products/cart_detail.html', {'cart': cart})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart  # Atualiza o carrinho na sessão
    return redirect('cart_detail')

def finalize_purchase(request):
    cart = request.session.get('cart', {})

    if not cart:
        messages.error(request, "Seu carrinho está vazio!")
        return redirect('cart_detail')

    with transaction.atomic():
        orders = []  # Lista para armazenar os pedidos criados
        total_price = 0

        for product_id, item in cart.items():
            product = get_object_or_404(Product, id=product_id)

            if product.stock >= item['quantity']:
                order = Order.objects.create(
                    user=request.user,
                    product=product,
                    quantity=item['quantity'],
                    total_price=item['quantity'] * product.price,
                )
                product.stock -= item['quantity']
                product.save()
                orders.append(order)
                total_price += order.total_price
            else:
                messages.error(request, f"Estoque insuficiente para o produto {product.name}.")
                return redirect('cart_detail')

        # Simular pagamento
        payment_status = simulate_payment(total_price)

        # Atualizar o status de cada pedido
        for order in orders:
            order.status = payment_status
            order.save()

        if payment_status == 'PAID':
            request.session['cart'] = {}  # Limpar o carrinho
            messages.success(request, "Compra realizada com sucesso.")
        else:
            messages.error(request, "Pagamento falhou. Tente novamente.")

    return redirect('product_list')


def simulate_payment(total):
    """
    Simula um endpoint de pagamento.
    Retorna 'PAID' ou 'FAILED' com base em uma lógica aleatória.
    """
    # Simule o sucesso do pagamento com 80% de probabilidade
    if random.random() < 0.8:
        return 'PAID'
    return 'FAILED'

# Para transformar em micro servviço, substituir a função acima "Simulate Payment" por essa abaixo:

#def process_payment(total):
#    response = requests.post('http://payment-microservice-url/pay', json={'total': total})
#    return response.json().get('status', 'FAILED')

def finalize_purchase_backend(request):
    if request.method == "POST":
        cart = request.session.get('cart', {})

        if not cart:
            messages.error(request, "Seu carrinho está vazio!")
            return redirect('product_list')

        # Processar cada item no carrinho
        for product_id, item in cart.items():
            product = get_object_or_404(Product, id=product_id)
            
            # Criar o pedido na tabela Order
            Order.objects.create(
                user=request.user,
                product=product,
                quantity=item['quantity'],
                total_price=item['quantity'] * product.price,
            )

            # Atualizar o estoque
            product.stock -= item['quantity']
            product.save()

        # Limpar o carrinho
        request.session['cart'] = {}

        # Mensagem de sucesso
        messages.success(request, "Compra finalizada com sucesso! Obrigado pela preferência.")

        return redirect('product_list')





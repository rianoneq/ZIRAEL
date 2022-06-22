from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from django.http import JsonResponse


def cart_add(request, product_slug, quantity):
  cart = Cart(request)

  product = get_object_or_404(Product, slug=product_slug)
  quantity = int(quantity)
  
  cart.add(product=product,
            quantity=quantity,
            update_quantity=False)

  total_count = cart.__len__()

  return JsonResponse({'total_count': total_count}, safe=False)

def cart_remove(request, product_slug):
  cart = Cart(request)
  product = get_object_or_404(Product, slug=product_slug)
  cart.remove(product)

  total_count = cart.__len__()
  total_price = cart.get_total_price()

  return JsonResponse({'total_count': total_count, 'total_price': total_price}, safe=False)


def cart_detail(request):
  cart = Cart(request)
  return render(request, 'cart/detail.html', {'cart': cart, 'page_title': 'Корзина' })
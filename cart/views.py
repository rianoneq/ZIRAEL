from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# @require_POST
def cart_add(request, product_slug, quantity):
  cart = Cart(request)

  product = get_object_or_404(Product, slug=product_slug)
  total_count = cart.__len__
  quantity = int(quantity)
  
  cart.add(product=product,
            quantity=quantity,#cd['quantity']
            update_quantity=False)#cd['update']
  

  return render(request, 'cart/count.html', {'total_count': total_count})

def cart_remove(request, product_slug):
  cart = Cart(request)
  product = get_object_or_404(Product, slug=product_slug)
  cart.remove(product)
  return redirect('cart:cart_detail')

def cart_detail(request):
  cart = Cart(request)
  return render(request, 'cart/detail.html', {'cart': cart, 'page_title': 'Корзина' })
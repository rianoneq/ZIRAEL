from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_slug):
  cart = Cart(request)

  product = get_object_or_404(Product, slug=product_slug)
  form = CartAddProductForm(request.POST)
  if form.is_valid():
    cd = form.cleaned_data
    cart.add(product=product,
              quantity=cd['quantity'],
              update_quantity=cd['update'])
  return redirect(f'/catalog/{product.slug}')

def cart_remove(request, product_slug):
  cart = Cart(request)
  product = get_object_or_404(Product, slug=product_slug)
  cart.remove(product)
  return redirect('cart:cart_detail')

def cart_detail(request):
  cart = Cart(request)
  return render(request, 'cart/detail.html', {'cart': cart, 'page_title': 'Корзина' })
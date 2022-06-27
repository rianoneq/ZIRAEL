from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Order, OrderItem
from django.views import generic
from django.contrib.auth.decorators import login_required

# from .tasks import order_created


class OrderDetailView(generic.DetailView):
    model = Order

    def get_context_data(self, **kwargs):

        # В первую очередь получаем базовую реализацию контекста
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        order_id = self.kwargs['pk']
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['order_products'] = OrderItem.objects.filter(order=order_id)
        context['page_title'] = f'Мой заказ#{order_id}' 
        return context

def create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            total_price = cart.get_total_price()
            total_count = cart.__len__()
            if total_price > 0 and total_count > 0:
            
                order = form.save(commit=False)
                order.user = request.user

                # set order total price and count here
                order.total_price = total_price
                order.total_count = total_count
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                            product=item['product'],
                                            price=item['price'],
                                            quantity=item['quantity'])
                # очистка корзины

                cart.clear()
                # запуск асинхронной задачи
                # order_created.delay(order.id)
                return render(request, 'orders/created.html',
                            {'order': order, 'page_title': 'Заказ успешно создан!'})
            else:
                return redirect('cart:cart_detail')
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'cart': cart, 'form': form, 'page_title': 'Создание заказа...'})


def check_order_status(request, bill_id):
    order = Order.objects.filter(order_id=bill_id).first()
    
    st = order.check_bill_status(order.bill_id)
    return JsonResponse({
        'success': st
    })

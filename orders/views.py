from django.http import JsonResponse
from django.shortcuts import redirect, render

from main.handlers import ajax_required
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import Order, OrderItem
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

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

def can_user_create_order(user):
    waiting_orders = Order.objects.filter(user=user).filter(status__exact='WA')

    if len(waiting_orders) < 4:
        return True

    return False

@login_required
def create(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    total_count = cart.__len__()
    if total_price > 0 and total_count > 0:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)

            if not request.user:
                raise Exception

            can_create_order = can_user_create_order(user=request.user)
            if can_create_order:
                if form.is_valid():
                    
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
                return render(request, 'orders/create.html',{'form':form, 'errors': ['У Вас уже висит 1 неоплаченный заказ. Пока он не истечет или не будет оплачен, вы не сможете создавать другие.']})
        else:
            form = OrderCreateForm
        return render(request, 'orders/create.html',
                    {'cart': cart, 'form': form, 'page_title': 'Создание заказа...'})
    else:
        return redirect('cart:cart_detail')


@ajax_required
def check_order_status(request):
    bill_id = request.POST.get('bill_id')
    statuses = {
        'PAID': 'PD',
        'EXPIRED': 'EX',
        'WAITING': 'WA',
        'REJECTED': 'RE'
    }

    order = Order.objects.filter(order_id=bill_id).first()
    current_order_status_in_db = order.status

    data = order.check_bill_status(order.bill_id)
    real_order_status = data['status']

        
    if not data:
        raise Exception('Похоже вы не оплатили, либо заказ уже истек')
    
    if current_order_status_in_db != statuses[real_order_status]:
        Order.objects.filter(order_id=bill_id).update(status=statuses[real_order_status])
        

    return JsonResponse({
        'data': data
    })

@ajax_required
def get_order_data(request):
    order_id = request.POST.get('order_id')
    order = Order.objects.filter(id=order_id).first()
    
    return JsonResponse({'success': True, 'data': {'order_status': order.status}}, safe=False)
    
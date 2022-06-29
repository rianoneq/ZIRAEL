from os import stat
import re
from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from django.urls import reverse
from .qiwi import create_bill, _check_bill_status

class Order(models.Model):

  status_choices = (
    ('PD', 'PAID'),
    ('EX', 'EXPIRED'),
    ('WA', 'WAITING'),
    ('RE', 'REJECTED'),
  )

  user = models.ForeignKey(User, related_name='user', on_delete=models.SET_NULL, null=True)
  order_id = models.CharField(max_length=100, blank=True)#, default=get_order_data
  bill_id = models.CharField(max_length=100, blank=True)#, default=get_order_data
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  total_price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
  total_count = models.PositiveIntegerField(default=1)

  email = models.EmailField()
  address = models.CharField(max_length=250)
  postal_code = models.CharField(max_length=20)
  city = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=2, choices=status_choices, default='WA')


  def get_order_data(self):
    # amount и comment генерируются не из функций, т.к
    # почему то после form.save() данные корзины очищаются и я не могу
    # использовать функции get_total_count и get_total_price

    # поэтому в файле представлений, в момент, когда форму заполнили и отправили
    # присваиваются корректные значения стоимости заказа и количества товаров

    amount = self.total_price
    lifetime = 20
    comment = f'buying {self.total_count} items in zirael shop'

    bill = create_bill(amount=amount,  
                       lifetime=lifetime,
                       comment=comment)

    order_id = bill.pay_url.split('=')[1]
    bill_id = bill.bill_id
    
    return {'order_id':order_id,
            'bill_id':bill_id}
  
  def get_total_count(self):
    return sum(item.quantity for item in self.items.all())

  def get_total_price(self):
    return sum(item.get_cost() for item in self.items.all())
  
  def get_absolute_url(self):
    return reverse('order:order_detail_view', args=[str(self.id)])

  def check_bill_status(self, bill_id):
    checker_output = _check_bill_status(bill_id=bill_id)
    if checker_output['success']:
      return checker_output['data']
    raise Exception('Незвестная ошибка')

  def save(self, *args, **kwargs):
    data = self.get_order_data()
    self.order_id = data['order_id']
    self.bill_id = data['bill_id']
    super(Order, self).save(*args, **kwargs)

  class Meta:
    ordering = ('-created',)
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'

  def __str__(self):
    return f'order #{self.id}'

class OrderItem(models.Model):
  order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.PositiveIntegerField(default=1)

  def __str__(self):
    return f'{self.id}'

  def get_cost(self):
    return self.price * self.quantity

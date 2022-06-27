from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
  """
  Задача для отправки уведомления по электронной почте при успешном создании заказа. 
  """
  order = Order.objects.get(id=order_id)
  subject = 'Айди заказа. {}'.format(order_id)
  message = 'Привет {},\n\nТы успешно разместил закоз, айди которого.\
              {}.'.format(order.first_name,
                                            order.id)
  mail_sent =  send_mail(subject,
                message,
                'admin@zirael.com',
                [order.email])
   
  return mail_sent
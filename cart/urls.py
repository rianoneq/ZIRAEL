from django.urls import re_path

from . import views


urlpatterns = [
    re_path(r'^$', views.cart_detail, name='cart_detail'),
    re_path(r'^add/$', views.cart_add, name='cart_add'),
    re_path(r'^remove/$', views.cart_remove, name='cart_remove'),
]
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^check/', views.check_order_status, name='check_order_status'),
    re_path(r'^create/', views.create, name='create'),
    re_path(r'^order/(?P<pk>[\d]+)$', views.OrderDetailView.as_view(), name='order_detail_view'),
]
from django.urls import re_path
from . import views

urlpatterns = [
  re_path(r'^user/$', views.user_data, name='user'),  
  re_path(r'^signup/$', views.SignUpView.as_view(), name='singup'),
]
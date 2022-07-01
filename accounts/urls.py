from django.urls import re_path
from . import views



urlpatterns = [
  re_path(r'^user/$', views.user_data, name='user'),  
  re_path(r'^login/$', views.user_login, name='login'),  
  re_path(r'^signup/$', views.signup, name='signup'),
]
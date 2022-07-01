from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def user_logout(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('catalog:catalog_page')
  else:
    return HttpResponse('You are not logged in!')

@login_required
def user_data(request):
  orders = Order.objects.filter(user=request.user)
  return render(request, 'accounts/user_detail.html', {'orders': orders, 'page_title': f'Страница юзера {request.user}'})



class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"
  
  
  def get_context_data(self, **kwargs):

    context = super(SignUpView, self).get_context_data(**kwargs)
    context['page_title'] = 'Регистрация'
    return context
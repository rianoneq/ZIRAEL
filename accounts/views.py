from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(username=cd['username'], password=cd['password'], email=cd['email'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('catalog:catalog_page')
        else:
          return HttpResponse('Disabled account')
      else:
        return HttpResponse('Invalid login')
  else:
    form = LoginForm()
  return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('catalog:catalog_page')
  else:
    return HttpResponse('You are not logged in!')

@login_required

def user_data(request):
  return JsonResponse({'user': request.user.is_authenticated,
                       'username': request.user.username,
                       'email': request.user.email})

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"

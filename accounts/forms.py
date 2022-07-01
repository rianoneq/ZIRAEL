from cProfile import label
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].label = 'Юзернейм'
    self.fields['password'].label = 'Пароль'

  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)





class UserRegistrationForm(forms.ModelForm):

  password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

  class Meta:
    model = User
    fields = ('username',)
    labels = {
        "username": "Юзернейм",
    }
    help_texts = {
        'username': None,
    }

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError('Пароли не совпадают')
    return cd['password2']


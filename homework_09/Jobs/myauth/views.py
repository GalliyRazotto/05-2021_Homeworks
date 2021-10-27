from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from myauth.forms import MyUserCreationForm
from myauth.models import MyUser


class MyLoginView(LoginView):
    pass


class MyLogoutView(LogoutView):
    pass


class CreateUserView(CreateView):
    model = MyUser
    success_url = reverse_lazy('list')
    form_class = MyUserCreationForm

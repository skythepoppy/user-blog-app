from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm as usc
from django.urls import reverse_lazy

class UserRegister(generic.CreateView):
    form_class = usc
    template = 'registration/registration.html'
    success_url = reverse_lazy('login')


# Create your views here.

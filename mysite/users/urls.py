from django.urls import path
from . views import UserRegister

url_patterns= [
    path('register/', UserRegister.as_view(), name='register')

]
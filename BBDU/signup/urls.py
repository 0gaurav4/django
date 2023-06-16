from operator import index
from django.contrib import admin
from django.urls import path
from signup.views import signup, success
from signup.views import signup, success, logout_view

urlpatterns = [
    path('', signup, name='signup'),
    path('index/', index, name='index'),
    path('success/', success, name='success'),
    path('logout/', success, name='logout'),
]

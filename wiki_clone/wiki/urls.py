from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<str:title>/', views.page, name='page'),
    path('page/<str:title>/edit/', views.edit_page, name='edit_page'),
    path('page/<str:title>/save/', views.save_page, name='save_page'),
]

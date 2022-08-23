from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dolar/', views.dollar, name='dolar'),
    path('Error404/', views.Error404, name='error404'),
]

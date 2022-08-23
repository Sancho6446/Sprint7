from django.urls import path
from . import views
from Login.views import sign_out

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dolar/', views.dollar, name='dolar'),
    path('sign-out/', sign_out, name='sign out'),
]

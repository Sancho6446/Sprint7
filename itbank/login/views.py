from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from cuentas.models import Cliente, Cuenta
from login.models import Usuario


def create_context(username):
    customer_id = Usuario.objects.get(
        username=username).customer_id

    cliente = Cliente.objects.get(
        customer_id=customer_id)

    cuenta = Cuenta.objects.get(
        account_id=customer_id)

    limites = {1: 100000, 2: 300000, 3: 500000}

    return {'cliente': cliente, 'username': username, 'cuenta': cuenta, 'limite': limites[cuenta.account_type.act_id]}

def loginPage(request):
    page='login.html'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
        else:
            messages.error(request, 'El usuario o la contraseña es incorrecta')

    context = {'page': page}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from cuentas.models import Cliente, Cuenta
from login.models import Usuario

#from .models import Room, Topic
#from .forms import RoomForm



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

def existe_usuario(data):
    try:
        return Usuario.objects.get(Q(customer_id=data["customer_id"]) | Q(username=data['username']))
    except Usuario.DoesNotExist:
        return False


def is_valid(customer_id):
    try:
        return Cliente.objects.get(customer_id=customer_id)
    except Cliente.DoesNotExist:
        return False


def sign_up(request):
    if request.method == 'POST':
        customer_id = request.POST['customer_id']
        if is_valid(customer_id):
            if existe_usuario(request.POST):
                return render(request, 'login/login.html')
            else:
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
                usuario = Usuario.objects.create_user(
                    username=username, password=password, email=email)
                usuario.customer_id = customer_id
                usuario.save()
                user = authenticate(
                    request, username=username, password=password)

                if user:
                    login(request, user)

                    context = create_context(username)
                    return render(request, 'homepage/dashboard.html', context)

        return render(request, 'login/login.html')



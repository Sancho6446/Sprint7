from urllib.robotparser import RequestRate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home/index.html')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'home/dashboard.html')


def dollar(request):
    return render(request, 'home/dollar.html')


def Error404(request):
    return render(request, 'home/Error404.html')

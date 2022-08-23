from unicodedata import name
from django.shortcuts import render, redirect
from .forms import Prestamosform
from django.urls import reverse
# Create your views here.


def Prestamos(request):
    prestamos_form = Prestamosform()
    if request.method == "POST":
        if prestamos_form.is_valid():
            name = request.POST.get('name', '')
        return redirect(reverse('Prestamos')+"?ok")
    return render(request, "Prestamos/formulario.html", {'form': prestamos_form})

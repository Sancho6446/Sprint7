from turtle import resizemode
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login.views import create_context
from django.contrib import messages
from cuentas.models import Prestamo
import csv
from django.http import HttpResponse

@login_required(login_url='/login/')
def validation(request, username):
    if request.method == 'POST':
        context=create_context(username)
        if request.POST.get('action') == 'validate':
            if request.POST.get('amount') > context['limite']:
                messages.error(request, 'El monto supera el limite')
                return render(request, 'cuentas/dashboard.html', context)

            prestamo = Prestamo.objects.create(
                customer_id=context['cliente'],
                loan_date=request.POST.get('start-date'),
                loan_type=request.POST.get('loan-type'),
                loan_total=request.POST.get('amount'),
            )
            prestamo.save()
            report(prestamo)
            context['cuenta'].balance += prestamo.loan_total
            context['cuenta'].save()
            context['message'] = 'Prestamo realizado con exito'
            return render(request, 'cuentas/dashboard.html', context)
        elif request.POST.get('action') == 'cancel':
            context['message'] = 'Prestamo cancelado con exito'
            return render(request, 'cuentas/dashboard.html', context)
        else:
            return render(request, 'cuentas/dashboard.html', context)

def report(prestamo):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="prestamo.csv"'
    
    writer = csv.writer(response)
    
    prestamo = Prestamo.objects.all()

    writer.writerow(['Cliente', 'Balance Actual', 'Balance Nuevo', 'Monto Prestamo', 'Tipo de Prestamo', 'Fecha'])

    for p in prestamo:
        writer.writerow([p.customer.client_name, p.customer.balance, p.customer.balance + p.loan_total, p.loan_total, p.loan_type, p.loan_date])
    
    return response
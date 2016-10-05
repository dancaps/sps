from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth

from pet_sitting.forms import CustomerForm


def dashboard(request):
    context = {'html': 'THIS IS MY NEW CODE!'}
    return render(request, 'menu_sidebar.html')

def add_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
    else:
        customer_form = CustomerForm()

    context = {'customer_form': customer_form}

    return render(request, 'add_customer.html', context)


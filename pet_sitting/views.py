from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from pet_sitting.models import Customer, Pet, Order, Service

from pet_sitting.forms import CustomerForm, PetForm

def dashboard(request):
    context = {'html': 'THIS IS MY NEW CODE!'}
    return render(request, 'menu_sidebar.html')

def add_customer(request, customer_id=0):
    heading = 'Add New Customer'
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
    else:
        if customer_id == 0:
            customer_form = CustomerForm()
        else:
            customer_obj = Customer.objects.get(id=customer_id).__dict__
            customer_form = CustomerForm(initial=customer_obj)
            heading = 'Edit Customer: ' + customer_obj['first_name'] + ' ' +customer_obj['last_name']
    context = {'customer_form': customer_form, 'heading' : heading}
    return render(request, 'add_customer.html', context)

def add_pet(request):
    if request.method == 'POST':
        pet_form = PetForm(request.POST)
        if pet_form.is_valid():
            pet_form.save()
    else:
        pet_form = PetForm()
    context = {'pet_form': pet_form, }
    return render(request, 'add_pet.html', context)

def get_customers(request):
    return render(request, 'all_ids.html', {'ids' : Customer.objects.all(), 'url' : 'customer',
                                            'heading' : 'View All Customers', })

def get_customer(request, customer_id=1):
    context = {'id': Customer.objects.get(id=customer_id), 'url': 'customer',
               'heading': 'Edit Customer: ' + Customer.objects.get(id=customer_id).first_name +
                          ' ' + Customer.objects.get(id=customer_id).last_name, }
    return render(request, 'id.html', context)

def get_pets(request):
    return render(request, 'all_ids.html', {'ids': Pet.objects.all(), 'url' : 'pet', 'heading': 'All Pets', })

def get_pet(request, pet_id=1):
    context = {'id': Pet.objects.get(id=pet_id), 'url' : 'pet',
               'heading': 'Edit Pet: ' + Pet.objects.get(id=pet_id).name, }
    return render(request, 'id.html', context)
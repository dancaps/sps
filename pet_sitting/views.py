from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from pet_sitting.models import Customer, Pet, Order, Service
from pet_sitting.forms import CustomerForm, PetForm, OrderForm, ServiceForm


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'menu_sidebar.html')


@login_required(login_url='/login/')
def get_customers(request):
    return render(request, 'all_ids.html', {'ids': Customer.objects.all(), 'url': 'customer',
                                            'heading': 'View All Customers', })


@login_required(login_url='/login/')
def get_customer(request, customer_id=1):
    context = {'id': Customer.objects.get(id=customer_id), 'url': 'customer',
               'heading': 'Edit Customer: ' + Customer.objects.get(id=customer_id).first_name +
                          ' ' + Customer.objects.get(id=customer_id).last_name, }
    return render(request, 'id.html', context)


@login_required(login_url='/login/')
def add_customer(request, customer_id=0):
    customer_id = int(customer_id)
    heading = 'Add a New Customer'
    if request.method == 'POST':
        if customer_id > 0:
            customer_obj = Customer.objects.get(id=customer_id)
            customer_form = CustomerForm(request.POST, instance=customer_obj)
        else:
            customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return HttpResponseRedirect('/pet_sitting/customer/all/')
    else:
        if customer_id > 0:
            customer_form = CustomerForm()
        else:
            customer_obj = Customer.objects.get(id=customer_id)
            print(customer_obj)
            customer_form = CustomerForm(instance=customer_obj)
            heading = 'Edit Customer: ', customer_obj.first_name + ' ' + customer_obj.last_name
    context = {'add_form': customer_form, 'heading' : heading}
    return render(request, 'add_form.html', context)


@login_required(login_url='/login/')
def get_orders(request):
    return render(request, 'all_ids.html', {'ids': Order.objects.all(), 'url': 'order',
                                            'heading': 'View All Orders', })


@login_required(login_url='/login/')
def get_order(request, order_id=1):
    context = {'id': Order.objects.get(id=order_id), 'url': 'order',
               'heading': 'Edit Order: ' + Order.objects.get(id=order_id).customer.first_name +
                          ' ' + Order.objects.get(id=order_id).customer.last_name, }
    return render(request, 'id.html', context)


@login_required(login_url='/login/')
def add_order(request, order_id=0):
    heading = 'Add a New Order'
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return HttpResponseRedirect('/pet_sitting/order/all/')
    else:
        if order_id == 0:
            order_form = OrderForm()
        else:
            order_obj = Order.objects.get(id=order_id).__dict__
            order_form = OrderForm(initial=order_obj)
            heading = 'Edit Order: ' + str(order_obj['id'])
    context = {'add_form': order_form, 'heading' : heading}
    return render(request, 'add_form.html', context)


@login_required(login_url='/login/')
def get_pets(request):
    return render(request, 'all_ids.html', {'ids': Pet.objects.all(), 'url': 'pet', 'heading': 'All Pets', })


@login_required(login_url='/login/')
def get_pet(request, pet_id=1):
    context = {'id': Pet.objects.get(id=pet_id), 'url': 'pet',
               'heading': 'Edit Pet: ' + Pet.objects.get(id=pet_id).name, }
    return render(request, 'id.html', context)


@login_required(login_url='/login/')
def add_pet(request, pet_id=0):
    heading = 'Add a New Pet'
    if request.method == 'POST':
        pet_form = PetForm(request.POST)
        if pet_form.is_valid():
            pet_form.save()
            return HttpResponseRedirect('/pet_sitting/pet/all/')
    else:
        if pet_id == 0:
            pet_form = PetForm()
        else:
            pet_obj = Pet.objects.get(id=pet_id).__dict__
            pet_form = PetForm(initial=pet_obj)
            heading = 'Edit Pet: ' + pet_obj['name']
    context = {'add_form': pet_form, 'heading': heading}
    return render(request, 'add_form.html', context)


@login_required(login_url='/login/')
def get_services(request):
    return render(request, 'all_ids.html', {'ids': Service.objects.all(), 'url': 'service', 'heading': 'All Services', })


@login_required(login_url='/login/')
def get_service(request, service_id=1):
    context = {'id': Service.objects.get(id=service_id), 'url': 'service',
               'heading': 'Edit Service: ' + Service.objects.get(id=service_id).name, }
    return render(request, 'id.html', context)


@login_required(login_url='/login/')
def add_service(request, service_id=0):
    heading = 'Add a New Service'
    if request.method == 'POST':
        service_form = ServiceForm(request.POST)
        if service_form.is_valid():
            service_form.save()
            return HttpResponseRedirect('/pet_sitting/service/all/')
    else:
        if service_id == 0:
            service_form = ServiceForm()
        else:
            service_obj = Service.objects.get(id=service_id).__dict__
            service_form = ServiceForm(initial=service_obj)
            heading = 'Edit Service: ' + service_obj['name']
    context = {'add_form': service_form, 'heading': heading}
    return render(request, 'add_form.html', context)
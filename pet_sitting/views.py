import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from pet_sitting.models import Customer, Pet, Order, Service
from pet_sitting.forms import CustomerForm, PetForm, OrderForm, ServiceForm


@login_required(login_url='/login/')
def dashboard(request):
    active_orders = Order.objects.filter(start_date__lte=datetime.date.today()).filter(end_date__gte=datetime.date.today())
    active_orders = active_orders.order_by('end_date')
    unpaid_orders = Order.objects.filter(paid=False)
    upcoming_orders = Order.objects.filter(start_date__gt=datetime.date.today())
    context = {'active_orders': active_orders,
               'unpaid_orders': unpaid_orders,
               'upcoming_orders': upcoming_orders}
    return render(request, 'dashboard.html', context)


@login_required(login_url='/login/')
def get_customers(request):
    ids = Customer.objects.order_by('id')
    ids = ids.reverse()
    context = {'ids': ids,
               'url': 'customer',
               'heading': 'View All Customers', }
    return render(request, 'all_ids.html', context)


@login_required(login_url='/login/')
def get_customer(request, customer_id=1):
    customer_obj = Customer.objects.get(id=customer_id)
    pet_obj = Pet.objects.filter(customer_id=customer_obj)
    order_obj = Order.objects.filter(customer_id=customer_obj)
    context = {'customer': customer_obj,
               'heading': 'Customer: ' + customer_obj.full_name,
               'pets': pet_obj,
               'orders': order_obj,
               'customer_heading': 'Owner',
               'pet_heading': 'Pets',
               'order_heading': 'Orders', }
    return render(request, 'get_cust.html', context)


@login_required(login_url='/login/')
def add_customer(request, customer_id=None):
    heading = 'Add a New Customer'
    if request.method == 'POST': # POST code
        if customer_id != None: # POST with an ID: POST EDIT CHANGES
            customer_obj = Customer.objects.get(id=customer_id)
            customer_form = CustomerForm(request.POST, instance=customer_obj)
        else: # POST for the first time: ADD VIEW
            customer_form = CustomerForm(request.POST)
        if customer_form.is_valid(): # validate the POST and save the data
            customer_form.save()
            return HttpResponseRedirect('/pet_sitting/dashboard/')
    elif customer_id == None: # GET first time code
        customer_form = CustomerForm()
    else: # GET entry that already exists: EDIT VIEW
        customer_obj = Customer.objects.get(id=customer_id)
        customer_form = CustomerForm(instance=customer_obj)
        heading = 'Edit Customer: ' + customer_obj.full_name
    context = {'add_form': customer_form, 'heading' : heading}
    return render(request, 'add_form.html', context)


@login_required(login_url='/login/')
def get_orders(request):
    ids = Order.objects.order_by('id')
    ids = ids.reverse()
    context = {'ids': ids,
               'url': 'order',
               'heading': 'View All Orders', }
    return render(request, 'all_ids.html', context)


@login_required(login_url='/login/')
def get_order(request, order_id=1):
    order_obj = Order.objects.get(id=order_id)
    context = {'order': order_obj,
               'heading': 'Order: ' + Order.objects.get(id=order_id).customer.full_name,
               'order_heading': 'Orders', }
    return render(request, 'get_order.html', context)


@login_required(login_url='/login/')
def add_order(request, order_id=None):
    heading = 'Add a New Order'
    if request.method == 'POST': # POST code
        if order_id != None: # POST with an ID: POST EDIT CHANGES
            order_obj = Order.objects.get(id=order_id)
            order_form = OrderForm(request.POST, instance=order_obj)
        else: # POST for the first time: ADD VIEW
            order_form = OrderForm(request.POST)
        if order_form.is_valid(): # validate the POST and save the data
            order_form.save()
            return HttpResponseRedirect('/pet_sitting/dashboard/')
    elif order_id == None: # GET first time code
        order_form = OrderForm()
    else: # GET entry that already exists: EDIT VIEW
        order_obj = Order.objects.get(id=order_id)
        order_form = OrderForm(instance=order_obj)
        heading = 'Edit Order: ' + str(order_obj.id)
    context = {'add_form': order_form, 'heading' : heading}
    return render(request, 'add_form.html', context)


@login_required(login_url='/login/')
def get_pets(request):
    ids = Pet.objects.order_by('id')
    ids = ids.reverse()
    context = {'ids': ids,
               'url': 'pet',
               'heading': 'All Pets', }
    return render(request, 'all_ids.html', context)


@login_required(login_url='/login/')
def get_pet(request, pet_id=1):
    pet_obj = Pet.objects.get(id=pet_id)
    customer_id = pet_obj.customer_id
    customer_obj = Customer.objects.get(id=customer_id)
    sibling_pets = Pet.objects.filter(customer_id=customer_id).exclude(id=pet_obj.id)
    order_obj = Order.objects.filter(customer_id=customer_obj)
    context = {'pet': pet_obj,
               'heading': 'Pet: ' + Pet.objects.get(id=pet_id).name,
               'pet_heading': 'Pet',
               'customer_heading': 'Owner',
               'customer': customer_obj,
               'sibling_heading': 'Sibling Animals',
               'siblings': sibling_pets,
               'order_heading': 'Orders',
               'orders': order_obj,}
    return render(request, 'get_pet.html', context)


@login_required(login_url='/login/')
def add_pet(request, pet_id=None):
    heading = 'Add a New Pet'
    if request.method == 'POST':
        if pet_id != None: # POST with an ID: POST EDIT CHANGES
            pet_obj = Pet.objects.get(id=pet_id)
            pet_form = PetForm(request.POST, instance=pet_obj)
        else: # POST for the first time: ADD VIEW
            pet_form = PetForm(request.POST)
        if pet_form.is_valid(): # validate the POST and save the data
            pet_form.save()
            return HttpResponseRedirect('/pet_sitting/dashboard/')
    elif pet_id == None: # GET first time code
        pet_form = PetForm()
    else: # GET entry that already exists: EDIT VIEW
        pet_obj = Pet.objects.get(id=pet_id)
        pet_form = PetForm(instance=pet_obj)
        heading = 'Edit Pet: ' + pet_obj.name
    context = {'add_form': pet_form, 'heading': heading}
    return render(request, 'add_form.html', context)


@login_required(login_url='/login/')
def get_services(request):
    ids = Service.objects.order_by('id')
    ids = ids.reverse()
    context = {'ids': ids,
               'url': 'service',
               'heading': 'All Services', }
    return render(request, 'all_ids.html', context)


@login_required(login_url='/login/')
def get_service(request, service_id=1):
    context = {'service': Service.objects.get(id=service_id),
               'heading': 'Service: ' + Service.objects.get(id=service_id).name,
               'service_heading': 'Service', }
    return render(request, 'get_service.html', context)


@login_required(login_url='/login/')
def add_service(request, service_id=None):
    heading = 'Add a New Service'
    if request.method == 'POST':
        if service_id != None: # POST with an ID: POST EDIT CHANGES
            service_obj = Service.objects.get(id=service_id)
            service_form = ServiceForm(request.POST, instance=service_obj)
        else: # POST for the first time: ADD VIEW
            service_form = ServiceForm(request.POST)
        if service_form.is_valid(): # validate the POST and save the data
            service_form.save()
            return HttpResponseRedirect('/pet_sitting/dashboard/')
    elif service_id == None: # GET first time code
            service_form = ServiceForm()
    else: # GET entry that already exists: EDIT VIEW
        service_obj = Service.objects.get(id=service_id)
        service_form = ServiceForm(instance=service_obj)
        heading = 'Edit Service: ' + service_obj.name
    context = {'add_form': service_form, 'heading': heading}
    return render(request, 'add_form.html', context)


@login_required(login_url='/login/')
def search_results(request):
    search_query = request.POST.get('search_query', '')
    context = {'message': None, 'heading': 'Search Results: ' + search_query, 'customer_results': None,
               'pet_results': None, }
    if len(search_query) == 0:
        context['message'] = 'There were 0 results returned'
        return render(request, 'page_content.html', context)
    customer_result = Customer.customer_search(search_query)
    pet_result = Pet.pet_search(search_query)
    context['customer_results'] = customer_result
    context['pet_results'] = pet_result
    context['message'] = 'There were ' + str(len(customer_result) + len(pet_result)) + ' results returned'
    return  render(request, 'page_content.html', context)
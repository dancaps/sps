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
               'heading': 'Customer: ' + Customer.objects.get(id=customer_id).first_name +
                          ' ' + Customer.objects.get(id=customer_id).last_name, }
    return render(request, 'id.html', context)


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
            return HttpResponseRedirect('/pet_sitting/customer/all/')
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
    return render(request, 'all_ids.html', {'ids': Order.objects.all(), 'url': 'order',
                                            'heading': 'View All Orders', })


@login_required(login_url='/login/')
def get_order(request, order_id=1):
    context = {'id': Order.objects.get(id=order_id), 'url': 'order',
               'heading': 'Order: ' + Order.objects.get(id=order_id).customer.first_name +
                          ' ' + Order.objects.get(id=order_id).customer.last_name, }
    return render(request, 'id.html', context)


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
            return HttpResponseRedirect('/pet_sitting/order/all/')
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
    return render(request, 'all_ids.html', {'ids': Pet.objects.all(), 'url': 'pet', 'heading': 'All Pets', })


@login_required(login_url='/login/')
def get_pet(request, pet_id=1):
    context = {'id': Pet.objects.get(id=pet_id), 'url': 'pet',
               'heading': 'Pet: ' + Pet.objects.get(id=pet_id).name, }
    return render(request, 'id.html', context)


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
            return HttpResponseRedirect('/pet_sitting/pet/all/')
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
    return render(request, 'all_ids.html', {'ids': Service.objects.all(), 'url': 'service', 'heading': 'All Services', })


@login_required(login_url='/login/')
def get_service(request, service_id=1):
    context = {'id': Service.objects.get(id=service_id), 'url': 'service',
               'heading': 'Service: ' + Service.objects.get(id=service_id).name, }
    return render(request, 'id.html', context)


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
            return HttpResponseRedirect('/pet_sitting/service/all/')
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
               'pet_results': None, 'order_results': None}
    if len(search_query) == 0:
        context['message'] = 'There were 0 results returned'
        return render(request, 'page_content.html', context)
    customer_result = Customer.customer_search(search_query)
    pet_result = Pet.pet_search(search_query)
    #order_result = Order.order_search(search_query)
    context['customer_results'] = customer_result
    context['pet_results'] = pet_result
    #context['order_results'] = order_result
    context['message'] = 'There were ' + str(len(customer_result) + len(pet_result)) + ' results returned'
    return  render(request, 'page_content.html', context)
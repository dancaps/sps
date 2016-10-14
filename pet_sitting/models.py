from __future__ import unicode_literals
from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField

class Customer(models.Model):
    signup_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = USStateField()
    zip_code = USZipCodeField()
    primary_phone = PhoneNumberField(blank=True, null=True)
    secondary_phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    vet_name = models.CharField(max_length=200, blank=True, null=True)
    vet_phone = PhoneNumberField(blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=200, blank=True, null=True)
    emergency_contact_phone = PhoneNumberField(blank=True, null=True)
    contract_on_file = models.BooleanField()
    left_rating = models.BooleanField()
    allows_pics = models.BooleanField()
    mileage = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} {}, {}, {}'.format(self.first_name, self.last_name, self.primary_phone, self.email)

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @staticmethod
    def all_fields():
        # return ['signup_date', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'primary_phone',
        #         'secondary_phone', 'email', 'vet_name', 'vet_phone', 'emergency_contact_name', 'emergency_contact_phone',
        #         'contract_on_file', 'left_rating', 'allows_pics', 'mileage', 'notes', ]
        return ['first_name', 'last_name', 'street_address', 'city', 'state', 'email', 'vet_name', 'emergency_contact_name', 'notes', ]


        #kwargs = {i: 'danny' for i in customer_fields}
        #Customer.objects.filter(**kwargs)
        #maybe 2 methods 1 for int and 1 for string
        # do a check for data type coming in from the search, then pull the proper method, build the kwargs and filter the results
        # kwargs = {i + '__icontains': 'superior' for i in customer_fields}
        # for k, v in kwargs.items():
        #     args = {k: v}
        #     l_cust.append(Customer.objects.filter(**args))
        # results = []
        # for i in l_cust:
        #     if len(i) > 1:
        #         results += i
        # results


class Pet(models.Model):
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer)
    animal_type = models.CharField(max_length=200)

    def __str__(self):
        return 'Owner: {} {} - Pet Name: {} - Animal: {}'.format(self.customer.first_name, self.customer.last_name,
                                                                 self.name, self.animal_type)

class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return 'Service: {} - Price: ${}'.format(self.name, self.price)

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    total_visits = models.IntegerField(null=True)
    total_mileage = models.IntegerField(null=True, blank=True) #can I populate this with customer mileage * num_visits
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) #can I populate this services.price
    pets = models.ManyToManyField(Pet) #I only want the customers pets to show up.
    services = models.ForeignKey(Service, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        #services = '-'.join([str(service.name) for service in self.services.get_queryset()])
        return 'Order Number: {}, ' \
               'Customer: {} {}, ' \
               'Start Date: {}, ' \
               'End Date: {}, ' \
               'Amount Due: {}, ' \
               'Paid: {}'.format(self.id, self.customer.first_name, self.customer.last_name, self.start_date,
                                 self.end_date, self.amount_due, self.paid)
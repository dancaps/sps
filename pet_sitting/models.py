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
    def customer_search(search_query):
        customers = []
        kwargs = {}
        is_string = False
        try:
            search_query = int(search_query)
        except:
            is_string = True

        fields =  {'first_name': 'string', 'last_name': 'string', 'street_address': 'string', 'city': 'string',
                   'state': 'string', 'zip_code': 'integer', 'primary_phone': 'integer', 'secondary_phone': 'integer',
                   'email': 'string', 'vet_name': 'string', 'vet_phone': 'integer', 'emergency_contact_name': 'string',
                   'emergency_contact_phone': 'integer', 'mileage': 'integer', 'notes': 'string'}

        for k, v in fields.items():
            if v == 'string':
                if is_string == True:
                    kwargs.update({k + '__icontains': search_query})
                else:
                    continue
            elif v == 'integer':
                if is_string == False:
                    kwargs.update({k + '__icontains': search_query})
                else:
                    continue

        for k, v in kwargs.items():
            args = {k: v}
            db_query = Customer.objects.filter(**args)
            customers += list(db_query)

        return list(set(customers))


class Pet(models.Model):
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer)
    animal_type = models.CharField(max_length=200)

    def __str__(self):
        return 'Owner: {} {} - Pet Name: {} - Animal: {}'.format(self.customer.first_name, self.customer.last_name,
                                                                 self.name, self.animal_type)

    @staticmethod
    def pet_search(search_query):
        pets = []
        kwargs = {}
        if type(search_query) == int:
            return pets

        fields = {'name': 'string', 'animal_type': 'string'}

        for k, v in fields.items():
            kwargs.update({k + '__icontains': search_query})

        for k, v in kwargs.items():
            args = {k: v}
            db_query = Pet.objects.filter(**args)
            pets += list(db_query)

        return list(set(pets))

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
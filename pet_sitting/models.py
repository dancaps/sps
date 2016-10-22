from __future__ import unicode_literals
from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField, \
                                  USZipCodeField


class Customer(models.Model):
    """
    This class is the customer database table. It contains a function
    that allows searching of filled.
    """
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
    emergency_contact_name = models.CharField(max_length=200,
                                              blank=True,
                                              null=True)
    emergency_contact_phone = PhoneNumberField(blank=True, null=True)
    contract_on_file = models.BooleanField()
    left_rating = models.BooleanField()
    allows_pics = models.BooleanField()
    mileage = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        This is the text that is returned with the object
        """
        return '{} {}, {}, {}'.format(self.first_name,
                                      self.last_name,
                                      self.primary_phone,
                                      self.email)

    @property
    def full_name(self):
        """
        :return: Custom property with the full name.
        """
        return '{} {}'.format(self.first_name,
                              self.last_name)

    @staticmethod
    def customer_search(search_query):
        """
        Searches the database fields for the search query provided.

        :param search_query: str/int: This param is created by
        request.POST and sent through views.py
        :return: Returns a list of objects that contains the search
        query in any of its fields.
        """

        customers = []
        kwargs = {}
        is_string = False

        # Tests the search_query to see if it's an integer or string.
        try:
            search_query = int(search_query)
        except:
            is_string = True

        # Manually created dict to define the field type. Either integer
        # or string. Any new fields that need to be included in the
        # search are required to be in this dict.
        fields = {'first_name': 'string',
                  'last_name': 'string',
                  'street_address': 'string',
                  'city': 'string',
                  'state': 'string',
                  'zip_code': 'integer',
                  'primary_phone': 'integer',
                  'secondary_phone': 'integer',
                  'email': 'string',
                  'vet_name': 'string',
                  'vet_phone': 'integer',
                  'emergency_contact_name': 'string',
                  'emergency_contact_phone': 'integer',
                  'mileage': 'integer',
                  'notes': 'string'}

        # Builds the dict with the fields of the same data type
        for k, v in fields.items():
            if v == 'string':
                if is_string:
                    kwargs.update({k + '__icontains': search_query})
                else:
                    continue
            elif v == 'integer':
                if not is_string:
                    kwargs.update({k + '__icontains': search_query})
                else:
                    continue

        # Takes the key:value pair, filters the fields and applies
        # any results to a list of objects.
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
        return 'Owner: {} {} - ' \
               'Pet Name: {} - ' \
               'Animal: {}'.format(self.customer.first_name,
                                   self.customer.last_name,
                                   self.name,
                                   self.animal_type)

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
        return 'Service: {} - Price: ${}'.format(self.name,
                                                 self.price)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    total_visits = models.IntegerField(null=True)
    total_mileage = models.IntegerField(null=True, blank=True)
    amount_due = models.DecimalField(max_digits=10,
                                     decimal_places=2,
                                     blank=True,
                                     null=True)
    services = models.ForeignKey(Service, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Order Number: {}, ' \
               'Customer: {} {}, ' \
               'Start Date: {}, ' \
               'End Date: {}, ' \
               'Amount Due: {}, ' \
               'Paid: {}'.format(self.id,
                                 self.customer.first_name,
                                 self.customer.last_name,
                                 self.start_date,
                                 self.end_date,
                                 self.amount_due,
                                 self.paid)

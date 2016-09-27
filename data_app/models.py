from __future__ import unicode_literals
from django.db import models
from django.utils.timezone import now
from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField

class TestingFields(models.Model):
    #signup_date = models.DateTimeField(auto_now_add=True) # saves the data/time into the field when the object is saved to the db
    #state = models.CharField(max_length=2) # I'm unsure why I can add more than 2 chars
    #zip = models.PositiveSmallIntegerField()
    #phone = models.PositiveIntegerField(blank=True) # I'm unsure why this makes me put in data
    #rating
    pass


class Customer(models.Model):
    signup_date = models.DateTimeField(auto_now_add=True)
    human_first_name = models.CharField(max_length=200)
    human_last_name = models.CharField(max_length=200)
    #pet_name = models.CharField(max_length=200) This is another table
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = USStateField()
    zip_code = USZipCodeField()
    primary_phone = PhoneNumberField()
    secondary_phone = PhoneNumberField()
    email = models.EmailField()
    vet_name = models.CharField(max_length=200)
    vet_phone = PhoneNumberField()
    emergency_contact_name = models.CharField(max_length=200)
    emergency_contact_phone = PhoneNumberField()
    contract_on_file = models.BooleanField()
    left_rating = models.BooleanField()
    allows_pics = models.BooleanField()

    def __unicode__(self):
        return 'Customer : {}'.format(self.human_first_name)

class Service(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __unicode__(self):
        return 'Service : {}, Costs : ${}'.format(self.name, self.price)

class Pet(models.Model):
    name = models.CharField(max_length=200, default='Katie')
    customer = models.ForeignKey(Customer, default=1)

    def __unicode__(self):
        return 'Pet Name : {} belongs to : {} {}'.format(self.name, self.customer.human_first_name,
                                                         self.customer.human_last_name)

class Order(models.Model):
    pass

def populate_db():
    a = Customers(human_first_name='Brad', human_last_name='Long', street_address='1 North Rd.',
                  city='Superior', state='CO', zip=12345, primary_phone=9234567890, secondary_phone=5126941175,
                  email='danny.caperton@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                  emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                  left_rating=False, allows_pics=True)
    a.save()
    b = Customers(human_first_name='Mike', human_last_name='Long', street_address='1 North Rd.',
                  city='Superior', state='CO', zip=12345, primary_phone=9234567890, secondary_phone=5126941175,
                  email='danny.caperton@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                  emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                  left_rating=False, allows_pics=True)
    b.save()
    c = Customers(human_first_name='Sarah', human_last_name='Long', street_address='1 North Rd.',
                  city='Superior', state='CO', zip=12345, primary_phone=9234567890, secondary_phone=5126941175,
                  email='danny.caperton@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                  emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                  left_rating=False, allows_pics=True)
    c.save()



from __future__ import unicode_literals
from django.db import models
from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField

class Customer(models.Model):
    signup_date = models.DateTimeField(auto_now_add=True)
    human_first_name = models.CharField(max_length=200)
    human_last_name = models.CharField(max_length=200)
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
    mileage = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} {}, {}, {}, {}'.format(self.human_first_name, self.human_last_name, self.primary_phone, self.email,
                                          self.notes)

class Pet(models.Model):
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer)
    animal_type = models.CharField(max_length=200)

    def __str__(self):
        return '{} is a {} that belongs to {} {}'.format(self.name, self.animal_type, self.customer.human_first_name,
                                                         self.customer.human_last_name)
class Service(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return 'Service = {}, Costs = ${}'.format(self.name, self.price)

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(auto_now_add=False)
    customer = models.ForeignKey(Customer)
    end_date = models.DateTimeField(auto_now_add=False)
    num_visits = models.IntegerField()
    mileage = models.IntegerField() #can I populate this with customer mileage * num_visits
    #amount_due = models.DecimalField(max_digits=10, decimal_places=2) #can I populate this services.price
    pets = models.ManyToManyField(Pet)
    services = models.ManyToManyField(Service)

    def __str__(self):
        services = '-'.join([str(service.name) for service in self.services.get_queryset()])
        return 'Order Information: OrderID = {}, ' \
               'Customer = {} {}, ' \
               'Services Requested = {}, ' \
               'Start Date = {}, ' \
               'End Date = {}'.format(self.id, self.customer.human_first_name, self.customer.human_last_name,
                                      services, self.start_date, self.end_date)

def populate_db(cust=3):
        count = 0
        while count < cust:
            a = Customer(human_first_name='Brad', human_last_name='Long', street_address='1 North Rd.',
                          city='Superior', state='CO', zip_code=12345, primary_phone=9234567890, secondary_phone=5126941175,
                          email='danny.caperton@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                          emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                          left_rating=False, allows_pics=True, mileage=10)
            a.save()
            b = Customer(human_first_name='Mike', human_last_name='Long', street_address='1 North Rd.',
                          city='Superior', state='CO', zip_code=12345, primary_phone=9234567890, secondary_phone=5126941175,
                          email='mike@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                          emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                          left_rating=False, allows_pics=True, mileage=7)
            b.save()
            c = Customer(human_first_name='Sarah', human_last_name='Long', street_address='1 North Rd.',
                          city='Superior', state='CO', zip_code=12345, primary_phone=9234567890, secondary_phone=5126941175,
                          email='sarah@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                          emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                          left_rating=False, allows_pics=True, mileage=4, notes='shitty customer')
            c.save()
            d = Pet(name='Fido', animal_type='Dog', customer=a)
            d.save()
            e = Pet(name='Benji', animal_type='Dog', customer=a)
            e.save()
            f = Pet(name='Cat', animal_type='Cat', customer=a)
            f.save()
            g = Pet(name='Fido', animal_type='Dog', customer=b)
            g.save()
            h = Pet(name='Bubbles', animal_type='Fish', customer=b)
            h.save()
            i = Pet(name='Piggy', animal_type='Guinea Pig', customer=b)
            i.save()
            j = Pet(name='Fishy', animal_type='Fish', customer=c)
            j.save()
            count += 1

        k = Service(name='Dog Walking', price=20.00)
        k.save()
        l = Service(name='Cat Sitting', price=15.00)
        l.save()
        m = Service(name='Overnight', price=65.00)
        m.save()
        n = Order(start_date='2017-01-01 12:00:01', customer=a, end_date='2017-02-01 12:00:01', num_visits=5, mileage=25)
        n.save()
        n.services.add(k)
        n.save()
        n.pets.add(d)
        n.save()
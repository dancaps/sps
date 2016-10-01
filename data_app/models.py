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
    primary_phone = PhoneNumberField()
    secondary_phone = PhoneNumberField(blank=True, null=True)
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
        return '{} {}, {}, {}'.format(self.first_name, self.last_name, self.primary_phone, self.email)

class Pet(models.Model):
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer)
    animal_type = models.CharField(max_length=200)

    def __str__(self):
        return 'Pet Name: {} - {} - Owner: {} {}'.format(self.name, self.animal_type, self.customer.first_name,
                                                         self.customer.last_name)
class Service(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return 'Service: {} - Price: ${}'.format(self.name, self.price)

class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, null=True)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    total_visits = models.IntegerField(null=True)
    total_mileage = models.IntegerField(null=True) #can I populate this with customer mileage * num_visits
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, null=True) #can I populate this services.price
    pets = models.ManyToManyField(Pet)
    services = models.ForeignKey(Service, null=True)

    def __str__(self):
        #services = '-'.join([str(service.name) for service in self.services.get_queryset()])
        return 'OrderID = {}, ' \
               'Customer: {} {}, ' \
               'Start Date: {}, ' \
               'End Date: {}'.format(self.id, self.customer.first_name, self.customer.last_name, self.start_date, self.end_date)

def populate_db(cust=3):
        count = 0
        while count < cust:
            a = Customer(first_name='Brad', last_name='Long', street_address='1 North Rd.',
                          city='Superior', state='CO', zip_code=12345, primary_phone=9234567890, secondary_phone=5126941175,
                          email='danny.caperton@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                          emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                          left_rating=False, allows_pics=True, mileage=10)
            a.save()
            b = Customer(first_name='Mike', last_name='Long', street_address='1 North Rd.',
                          city='Superior', state='CO', zip_code=12345, primary_phone=9234567890, secondary_phone=5126941175,
                          email='mike@gmail.com', vet_name='Billy Vetman', vet_phone=6549871321,
                          emergency_contact_name='Helen Keller', emergency_contact_phone=6549873215, contract_on_file=True,
                          left_rating=False, allows_pics=True, mileage=7)
            b.save()
            c = Customer(first_name='Sarah', last_name='Long', street_address='1 North Rd.',
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
        n = Order(start_date='2017-01-01', customer=a, end_date='2017-02-01', total_visits=5, total_mileage=25,
                  services=k, amount_due=100.00)
        n.save()
        # n.services.add(k)
        # n.save()
        n.pets.add(d)
        n.save()
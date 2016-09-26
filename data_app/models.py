from django.db import models
from django.utils.timezone import now

class TestingFields(models.Model):
    #signup_date = models.DateTimeField(auto_now_add=True) # saves the data/time into the field when the object is saved to the db
    #state = models.CharField(max_length=2) # I'm unsure why I can add more than 2 chars
    #zip = models.PositiveSmallIntegerField()
    #phone = models.PositiveIntegerField(blank=True) # I'm unsure why this makes me put in data
    rating

class Customers(models.Model):
    signup_date = models.DateTimeField(auto_now_add=True)
    human_first_name = models.CharField(max_length=50)
    human_last_name = models.CharField(max_length=100)
    #pet_name = models.CharField(max_length=200) This is another table
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.PositiveSmallIntegerField()
    primary_phone = models.PositiveIntegerField()
    #secondary_phone = models.PositiveIntegerField(blank=True)

    #def __str__(self):
    #    return 'First Name : ' + self.human_first_name #'/n' + 'Last Name : ' + self.human_last_name '/n' + 'Pet Name : ' + self.pet_name

    # email
    # vet_name
    # vet_phone
    # emergency_contact_name
    # emergency_contact_phone
    # contract_on_file
    # left_rating
    # allows_pics

class Services(models.Model):
    pass

class Pets(models.Model):
    pass

class Orders(models.Model):
    pass

def populate_db():
    a = Customers(human_first_name='Brad', human_last_name='Long', pet_name='Benji', street_address='1 North Rd.',
                  city='Superior', state='CO', zip=12345, primary_phone =9234567890,)
    a.save()
    b = Customers(human_first_name='Fred', human_last_name='Smith', pet_name='Fido', street_address='123 1st Rd.',
                  city='Superior', state='CO', zip=12345, primary_phone =3234567890,)
    b.save()
    c = Customers(human_first_name='Kathy', human_last_name='Clark', pet_name='Bubbles', street_address='987 15th St.',
                  city='Superior', state='CO', zip=12345, primary_phone =1234567890,)
    c.save()



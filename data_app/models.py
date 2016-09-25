from django.db import models

class Customers(models.Model):
    # signup_date
    human_first_name = models.CharField(max_length=200)
    human_last_name = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.PositiveSmallIntegerField()
    primary_phone = models.PositiveIntegerField()
    seconard_phone = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return 'First Name : ' + self.human_first_name #'/n' + 'Last Name : ' + self.human_last_name '/n' + 'Pet Name : ' + self.pet_name

    # email
    # vet_name
    # vet_phone
    # emergency_contact_name
    # emergency_contact_phone
    # contract_on_file
    # left_rating
    # allows_pics

#a = Customers(human_first_name='Brad', human_last_name='Long', pet_name='Benji', street_address='123 1st Rd.', city='Superior', state='CO', zip=12345, primary_phone =1234567890, secondary_phone=1987654321)




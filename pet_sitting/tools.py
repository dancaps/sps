from pet_sitting.models import *

"""
These are quick and dirty custom scripts that performed functions
during developement. This is ugly stuff.
"""

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
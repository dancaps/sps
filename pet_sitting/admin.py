from django.contrib import admin
from pet_sitting.models import Pet, Customer, Order, Service

admin.site.register(Pet)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Service)


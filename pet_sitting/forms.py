from django import forms
from pet_sitting.models import Customer, Pet, Service, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
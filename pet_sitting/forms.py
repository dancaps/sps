import datetime
from django import forms
from pet_sitting.models import Customer, Pet, Service, Order


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class OrderForm(forms.ModelForm):
    start_date = forms.DateField(initial=datetime.date.today,
                                 widget=forms.SelectDateWidget)
    end_date = forms.DateField(initial=datetime.date.today,
                               widget=forms.SelectDateWidget)
    class Meta:
        model = Order
        fields = ['customer',
                  'start_date',
                  'end_date',
                  'total_visits',
                  'amount_due',
                  'services',
                  'paid', ]


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
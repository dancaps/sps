from django.conf.urls import url, include
from pet_sitting.views import dashboard, add_customer, add_pet, get_customers, get_customer, get_pets, get_pet

urlpatterns = [
    #url(r'^$', login),
    url(r'^dashboard/$', dashboard),
    url(r'^add_customer/$', add_customer),
    url(r'^customer/all/$', get_customers),
    url(r'^customer/get/(?P<customer_id>\d+)/$', get_customer),
    url(r'^add_pet/$', add_pet),
    url(r'^pet/all/$', get_pets),
    url(r'^pet/get/(?P<pet_id>\d+)/$', get_pet),
]
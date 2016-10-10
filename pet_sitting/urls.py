from django.conf.urls import url, include
from pet_sitting.views import dashboard, add_customer, add_pet, get_customers, \
     get_customer, get_pets, get_pet, get_order, get_orders, add_order, get_services, get_service, add_service

urlpatterns = [
    #url(r'^$', login),
    url(r'^dashboard/$', dashboard),
    url(r'^add_customer/$', add_customer),
    url(r'^customer/all/$', get_customers),
    url(r'^customer/get/(?P<customer_id>\d+)/$', get_customer),
    url(r'^customer/edit/(?P<customer_id>\d+)/$', add_customer),
    url(r'^add_order/$', add_order),
    url(r'^order/all/$', get_orders),
    url(r'^order/get/(?P<order_id>\d+)/$', get_order),
    url(r'^order/edit/(?P<order_id>\d+)/$', add_order),
    url(r'^add_pet/$', add_pet),
    url(r'^pet/all/$', get_pets),
    url(r'^pet/get/(?P<pet_id>\d+)/$', get_pet),
    url(r'^pet/edit/(?P<pet_id>\d+)/$', add_pet),
    url(r'^add_service/$', add_service),
    url(r'^service/all/$', get_services),
    url(r'^service/get/(?P<service_id>\d+)/$', get_service),
    url(r'^service/edit/(?P<service_id>\d+)/$', add_service),
]
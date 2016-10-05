from django.conf.urls import url, include
from pet_sitting.views import dashboard, add_customer, add_pet

urlpatterns = [
    url(r'^$', dashboard),
    url(r'^add_customer/', add_customer),
    url(r'^add_pet/', add_pet),
]
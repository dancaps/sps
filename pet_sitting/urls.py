from django.conf.urls import url, include
from pet_sitting.views import dashboard, add_customer

urlpatterns = [
    url(r'^$', dashboard),
    url(r'^add_customer/', add_customer),
]
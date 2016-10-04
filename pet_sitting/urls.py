from django.conf.urls import url, include
from pet_sitting.views import landing_page

urlpatterns = [
    url(r'^$', landing_page),
]
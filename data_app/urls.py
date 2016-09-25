from django.conf.urls import url, include
from data_app.views import landing_page

urlpatterns = [
    url(r'^', landing_page),
]
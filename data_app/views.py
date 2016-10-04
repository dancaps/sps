from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def landing_page(request):
    context = {'html': 'THIS IS MY NEW CODE!'}
    return render(request, 'data_app.html', context)

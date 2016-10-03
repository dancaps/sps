from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth


def landing_page(request):
    html = "<h1>LANDING PAGE</h1>"
    return HttpResponse(html)

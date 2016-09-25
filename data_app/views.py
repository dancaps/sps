from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    html = "<h1>LANDING PAGE</h1>"
    return HttpResponse(html)

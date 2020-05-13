from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# views handles pages, routing etc

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hellow world</h1>")
    # return "<h1>Hello World<h2>" # its a string of html code


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>contacts</h1>")

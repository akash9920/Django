from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# views handles pages, routing etc

def home_view(request,*args, **kwargs):

   #2 return HttpResponse("<h1>Hellow world</h1>")
   # 1return "<h1>Hello World<h2>" # its a string of html code
   return render(request,"home.html",{})


def about_view(request,*args, **kwargs):
    return render(request,"about.html",{})

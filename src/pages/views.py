from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# views handles pages, routing etc

def home_view(request,*args, **kwargs):

   #2 return HttpResponse("<h1>Hellow world</h1>")
   # 1return "<h1>Hello World<h2>" # its a string of html code
   my_context = {
   "key1":"rhis is my data",
   "key2": 123456789,
   "key3" : ["akash","butter","chicken",
   "anand"]
   }
   return render(request,"home.html",my_context)


def about_view(request,*args, **kwargs):
    return render(request,"about.html",{})

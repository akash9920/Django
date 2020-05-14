from django.shortcuts import render

from .models import Product

def product_detail_view(request):

#	obj = Product.objects.get(id=1)
	#use object reference instead of each field in the context
#	context = {
#	'object' = obj
#	}
	return render(request,"product_detail.html",{})

# Create your views here.

from django.contrib import admin

#its the relative importing as they are in same folder

from .models import Product

admin.site.register(Product)
# Register your models here.

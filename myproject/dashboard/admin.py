from django.contrib import admin
from .models import Product
from .models import Order
from .models import Result
#from . import Newresult

from django.contrib.auth.models import Group

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'a', 'b', 'res')
    list_filter = ['id']

#class MynumberAdmin(admin.ModelAdmin):
    #list_display = ('a', 'b')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Result)
#admin.site.register(Mynumber, MynumberAdmin)
admin.site.site_header = "Jülich Dashboard"


#admin.site.unregister(Group)


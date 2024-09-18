from django.contrib import admin
from logistics.models import *

# Register your models here.
models = [SysUser, VehicleOwner, Vehicle, 
		  Driver, Shipment, Customer, 
		  Order, Location, Payment, 
		  Notification, Document, OrderStatusHistory]

for model in models:
	admin.site.register(model)
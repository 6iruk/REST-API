from django.contrib import admin
from .models import *

# Register your models here.
models = [Supplier, Driver, Product, Order]

for model in models:
	admin.site.register(model)
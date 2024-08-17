from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Supplier(models.Model):
   
   #Supplier's name
   name = models.CharField(max_length=20)

   #Supplier's phone number
   phone = models.CharField(max_length=20)

   #Supplier's products
   products = models.ManyToManyField('product')

   def __str__(self):
      return self.name + '/' + self.phone

   def add_product(self, product):
      #Add a product to supllier's list

      return self.products.add(product)


class Driver(models.Model):

   #Driver's name
   name = models.CharField(max_length=20)

   #Driver's phone number
   phone = models.CharField(max_length=20)

   #Driver's phone number
   phone = models.CharField(max_length=20)


   def __str__(self):
      return self.name + '/' + self.phone

   def add_order(self, order):
      #Add an order to driver's order list

      return self.orders.add(order)


class Product(models.Model):

   #Products name
   name = models.CharField(max_length=50, null=True)

   #Procducts price
   price = models.FloatField()

   #Products description
   description = models.CharField(max_length=200)

   def __str__(self):
      return self.name


class Order(models.Model):

   #Driver making the delivery
   driver = models.OneToOneField(Driver,  on_delete=models.DO_NOTHING)

   #Products to deliver
   products = models.ManyToManyField('product')

   #Order delivery address
   address = models.CharField(max_length=100)

   #Order total price
   price = models.FloatField()

   #Order amount
   amount = models.IntegerField(default=1)


   def __str__(self):
      return self.address + '-' + self.driver

   def add_product(self, product):
      #Add a product to order product list

      return self.products.add(product)
   
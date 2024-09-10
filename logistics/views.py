from django.shortcuts import render
from models import *
from serializers import *
from rest_framework import  viewsets


# Create your views here.
class SysUserViewSet(viewsets.ModelViewSet):

    queryset = SysUser.objects.all()
    serializer_class = SysUserSerializer

class VehicleOwnerViewSet(viewsets.ModelViewSet):

    queryset = VehicleOwner.objects.all()
    serializer_class = VehicleOwnerSerializer

class VehicleViewSet(viewsets.ModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class DriverViewSet(viewsets.ModelViewSet):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class ShipmentViewSet(viewsets.ModelViewSet):

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer

class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class LocationViewSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class NotificationViewSet(viewsets.ModelViewSet):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class DocumentViewSet(viewsets.ModelViewSet):

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class OrderStatusHistoryViewSet(viewsets.ModelViewSet):

    queryset = OrderStatusHistory.objects.all()
    serializer_class = OrderStatusHistorySerializer

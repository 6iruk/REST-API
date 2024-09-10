from rest_framework import serializers 
from models import *

class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = ['id', 'username','first_name', 'last_name', 'email', 'phone_number', 'role', 'date_joined', 'is_staff']

class VehicleOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleOwner
        fields = ['id', 'name', 'email', 'phone_number', 'bank_account', 'bank_name']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_type','plate_number', 'capacity', 'ownership_type', 'owner', 'registration_document', 'is_ready']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class OrderStatusHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusHistory
        fields = '__all__'
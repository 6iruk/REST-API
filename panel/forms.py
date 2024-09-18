from django.forms import ModelForm
from logistics.models import *

# Create the form class.

class SysUserForm(ModelForm):
    class Meta:
        model = SysUser
        fields = '__all__'

    field_order = ['first_name', 'last_name', 'phone_number', 'email', 'role', 'username']

class VehicleOwnerForm(ModelForm):
    class Meta:
        model = VehicleOwner
        fields = '__all__'

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class ShipmentForm(ModelForm):
    class Meta:
        model = Shipment
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

class OrderStatusHistoryForm(ModelForm):
    class Meta:
        model = OrderStatusHistory
        fields = '__all__'


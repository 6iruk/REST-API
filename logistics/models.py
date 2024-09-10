# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import RegexValidator

USER_ROLES = (
('DISPATCH', 'Dispatch'),
('DRIVER', 'Driver'),
('ADMIN', 'Admin'),
)
VEHICLE_TYPES = [
    ('TRUCK', 'Truck'),
    ('VAN', 'Van'),
    ('CAR', 'Car'),
]
OWNERSHIP_TYPES = [
    ('COMPANY', 'Company Owned'),
    ('RENTAL', 'Rental'),
    ('PRIVATE', 'Private'),
]
CUSTOMER_TYPES = [
    ('individual', 'Individual'),
    ('organization', 'Organization'),
]
ORDER_STATUS = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('PROCESSING', 'Processing'),
    ('ASSIGNED', 'Assigned'),
    ('IN_TRANSIT', 'In Transit'),
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled')
]
DOCUMENT_TYPES = (
    ('BANK_STATEMENT', 'Bank Statement'),
    ('INVOICE', 'Invoice'),
    ('RECEIPT', 'Receipt'),
    ('CONTRACT', 'Contract'),
    ('OTHER', 'Other'),
)

class SysUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True, unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    def __str__(self):
        return self.phone_number

class VehicleOwner(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True, null=True, blank=True)
    bank_account = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    plate_number = models.CharField(max_length=20, unique=True)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)  # in cubic meters
    ownership_type = models.CharField(max_length=20, choices=OWNERSHIP_TYPES)
    owner = models.ForeignKey(VehicleOwner, on_delete=models.CASCADE, related_name='vehicles')
    registration_document = models.FileField(upload_to='vehicle_documents/', null=True, blank=True)
    is_ready = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.get_vehicle_type_display()} - {self.plate_number}"

class Driver(models.Model):
    user = models.OneToOneField(SysUser, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    license_front = models.ImageField(upload_to='driver_licenses/')
    license_back = models.ImageField(upload_to='driver_licenses/')
    bank_account = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name()

class Shipment(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    material = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # in cubic meters
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    loaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.material
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='individual')
    notes = models.TextField(blank=True, null=True)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.address
    
class Order(models.Model):
    order_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='PENDING')
    delivery_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='delivery_orders')
    transport_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_number} for {self.customer.name}"

class Payment(models.Model):
    PAYMENT_TYPES = [
        ('SERVICE', 'Service Payment'),
        ('MATERIAL', 'Material Payment'),
        ('INTERMEDIARY', 'Intermediary Payment'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPES)
    bank = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    receipt_number = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment_type} for Order {self.order.order_number}"

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('SMS', 'SMS'),
        ('EMAIL', 'Email'),
        ('PUSH', 'Push Notification')
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.notification_type} for Order {self.order.order_number}"

class Document(models.Model):
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.get_document_type_display()} for {self.content_object}"

class OrderStatusHistory(models.Model):
    order = models.ForeignKey(Order, related_name='status_history', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Order.ORDER_STATUS)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(SysUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Status {self.status} for Order {self.order.order_number}"

    class Meta:
        ordering = ['-timestamp']

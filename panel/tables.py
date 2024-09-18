import django_tables2 as tables
from logistics.models import *

class SysUserTable(tables.Table):
    edit = tables.Column(default="Edit",linkify=True)

    class Meta:
        model = SysUser
        template_name = "panel/tables/bootstrap_htmx.html"

class VehicleOwnerTable(tables.Table):
    class Meta:
        model = VehicleOwner
        template_name = "panel/tables/bootstrap_htmx.html"

class VehicleTable(tables.Table):
    class Meta:
        model = Vehicle
        template_name = "tables/bootstrap_htmx.html"

class DriverTable(tables.Table):
    class Meta:
        model = Driver
        template_name = "tables/bootstrap_htmx.html"

class ShipmentTable(tables.Table):
    class Meta:
        model = Shipment
        template_name = "tables/bootstrap_htmx.html"

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        template_name = "tables/bootstrap_htmx.html"

class LocationTable(tables.Table):
    class Meta:
        model = Location
        template_name = "tables/bootstrap_htmx.html"

class OrderTable(tables.Table):
    class Meta:
        model = Order
        template_name = "tables/bootstrap_htmx.html"

class PaymentTable(tables.Table):
    class Meta:
        model = Payment
        template_name = "tables/bootstrap_htmx.html"

class NotificationTable(tables.Table):
    class Meta:
        model = Notification
        template_name = "tables/bootstrap_htmx.html"

class DocumentTable(tables.Table):
    class Meta:
        model = Document
        template_name = "tables/bootstrap_htmx.html"

class OrderStatusHistoryTable(tables.Table):
    class Meta:
        model = OrderStatusHistory
        template_name = "tables/bootstrap_htmx.html"


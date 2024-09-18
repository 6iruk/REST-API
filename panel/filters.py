from decimal import Decimal
from django.db.models import Q
import django_filters
from logistics.models import *

class SysUserFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = SysUser
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return SysUser.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return SysUser.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class VehicleOwnerFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = VehicleOwner
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return VehicleOwner.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return VehicleOwner.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class VehicleFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Vehicle
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Vehicle.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Vehicle.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class DriverFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Driver
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Driver.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Driver.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class ShipmentFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Shipment
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Shipment.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Shipment.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class CustomerFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Customer
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Customer.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Customer.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class LocationFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Location
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Location.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Location.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class OrderFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Order
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Order.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Order.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class PaymentFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Payment
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Payment.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Payment.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class NotificationFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Notification
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Notification.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Notification.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class DocumentFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Document
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return Document.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return Document.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )

class OrderStatusHistoryFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = OrderStatusHistory
        fields = ['query']

    def universal_search(self, queryset, name, value):
        if value.replace(".", "", 1).isdigit():
            value = Decimal(value)
            return OrderStatusHistory.objects.filter(
                Q(price=value) | Q(cost=value)
            )

        return OrderStatusHistory.objects.filter(
            Q(name__icontains=value) | Q(category__icontains=value)
        )



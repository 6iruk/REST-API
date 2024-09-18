from django.urls import path, include
from panel import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forms', views.forms, name='form'),
    path('user/', views.user, name='user-form'),
    path('owner/', views.owner, name='owner-form'),
    path('vehicle/', views.vehicle, name='vehicle-form'),
    path('driver/', views.driver, name='driver-form'),
    path('shipment/', views.shipment, name='shipment-form'),
    path('customer/', views.customer, name='customer-form'),
    path('location/', views.location, name='location-form'),
    path('order/', views.order, name='order-form'),
    path('payment/', views.payment, name='payment-form'),
    path('notification/', views.notification, name='notification-form'),
    path('document/', views.document, name='document-form'),
    path('status/', views.status, name='status-form'),
    path('list/user', views.SysUserTableView.as_view(), name='user-table'),
    path('list/owner', views.VehicleOwnerTableView.as_view(), name='owner-table'),
    path('list/vehicle', views.VehicleTableView.as_view(), name='vehicle-table'),
    path('list/driver', views.DriverTableView.as_view(), name='driver-table'),
    path('list/shipment', views.ShipmentTableView.as_view(), name='shipment-table'),
    path('list/customer', views.CustomerTableView.as_view(), name='customer-table'),
    path('list/location', views.LocationTableView.as_view(), name='location-table'),
    path('list/order', views.OrderTableView.as_view(), name='order-table'),
    path('list/payment', views.PaymentTableView.as_view(), name='payment-table'),
    path('list/notification', views.NotificationTableView.as_view(), name='notification-table'),
    path('list/document', views.DocumentTableView.as_view(), name='document-table'),
    path('list/status', views.OrderStatusHistoryTableView.as_view(), name='status-table'),

]
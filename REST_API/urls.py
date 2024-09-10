"""
URL configuration for REST_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from logistics.views import *
from rest_framework.routers import DefaultRouter

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'user', SysUserViewSet, basename='user')
router.register(r'owner', VehicleOwnerViewSet, basename='owner')
router.register(r'vehicle', VehicleViewSet, basename='vehicle')
router.register(r'driver', DriverViewSet, basename='driver')
router.register(r'shipment', ShipmentViewSet, basename='shipment')
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'location', LocationViewSet, basename='location')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'notification', NotificationViewSet, basename='notification')
router.register(r'document', DocumentViewSet, basename='document')
router.register(r'status', OrderStatusHistoryViewSet, basename='status')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

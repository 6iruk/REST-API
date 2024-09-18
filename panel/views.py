from django.shortcuts import render
import time
from panel.forms import *
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from logistics.models import *
from panel.tables import *
from panel.filters import *

# Create your views here.
def home(request):
    # Some processing 
    time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'panel/components/dashboard.html')
    else:
        return render(request, 'panel/components/dashboard_full.html')

def forms(request):
    # Some processing 
    time.sleep(0.5)
    # Processing End
    if request.htmx:
        return render(request, 'panel/components/forms_default.html')
    else:
        return render(request, 'panel/components/forms_default_full.html')

def user(request):

    if request.method == "POST":
        form = SysUserForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("user/")

    else:
        form = SysUserForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Users'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Users'})

def owner(request):

    if request.method == "POST":
        form = VehicleOwnerForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("owner/")

    else:
        form = VehicleOwnerForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Owner'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Owner'})

def vehicle(request):

    if request.method == "POST":
        form = VehicleForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("vehicle/")

    else:
        form = VehicleForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Vehicle'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Vehicle'})

def driver(request):

    if request.method == "POST":
        form = DriverForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("driver/")

    else:
        form = DriverForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Driver'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Driver'})

def shipment(request):

    if request.method == "POST":
        form = ShipmentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("shipment/")

    else:
        form = ShipmentForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Shipment'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Shipment'})

def customer(request):

    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("customer/")

    else:
        form = CustomerForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Customer'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Customer'})

def location(request):

    if request.method == "POST":
        form = LocationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("location/")

    else:
        form = LocationForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Location'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Location'})

def order(request):

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("order/")

    else:
        form = OrderForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Order'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Order'})

def payment(request):

    if request.method == "POST":
        form = PaymentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("payment/")

    else:
        form = PaymentForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Payment'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Payment'})

def notification(request):

    if request.method == "POST":
        form = NotificationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("notification/")

    else:
        form = NotificationForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Notification'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Notification'})

def document(request):

    if request.method == "POST":
        form = DocumentForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("document/")

    else:
        form = DocumentForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Document'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Document'})

def status(request):

    if request.method == "POST":
        form = OrderStatusHistoryForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("status/")

    else:
        form = OrderStatusHistoryForm()

    if request.htmx:
        return render(request, 'panel/components/forms.html', {"form": form, "header":'Status'})
    else:
        return render(request, 'panel/components/forms_full.html', {"form": form, "header":'Status'})

class SysUserTableView(SingleTableMixin, FilterView):
    table_class = SysUserTable
    queryset = SysUser.objects.all()
    filterset_class = SysUserFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "panel/components/tables.html"
        else:
            template_name = "panel/components/tables_full.html"

        return template_name

class VehicleOwnerTableView(SingleTableMixin, FilterView):
    table_class = VehicleOwnerTable
    queryset = VehicleOwner.objects.all()
    filterset_class = VehicleOwnerFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "panel/components/tables.html"
        else:
            template_name = "panel/components/tables_full.html"

        return template_name

class VehicleTableView(SingleTableMixin, FilterView):
    table_class = VehicleTable
    queryset = Vehicle.objects.all()
    filterset_class = VehicleFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class DriverTableView(SingleTableMixin, FilterView):
    table_class = DriverTable
    queryset = Driver.objects.all()
    filterset_class = DriverFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class ShipmentTableView(SingleTableMixin, FilterView):
    table_class = ShipmentTable
    queryset = Shipment.objects.all()
    filterset_class = ShipmentFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class CustomerTableView(SingleTableMixin, FilterView):
    table_class = CustomerTable
    queryset = Customer.objects.all()
    filterset_class = CustomerFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class LocationTableView(SingleTableMixin, FilterView):
    table_class = LocationTable
    queryset = Location.objects.all()
    filterset_class = LocationFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class OrderTableView(SingleTableMixin, FilterView):
    table_class = OrderTable
    queryset = Order.objects.all()
    filterset_class = OrderFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class PaymentTableView(SingleTableMixin, FilterView):
    table_class = PaymentTable
    queryset = Payment.objects.all()
    filterset_class = PaymentFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class NotificationTableView(SingleTableMixin, FilterView):
    table_class = NotificationTable
    queryset = Notification.objects.all()
    filterset_class = NotificationFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class DocumentTableView(SingleTableMixin, FilterView):
    table_class = DocumentTable
    queryset = Document.objects.all()
    filterset_class = DocumentFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name

class OrderStatusHistoryTableView(SingleTableMixin, FilterView):
    table_class = OrderStatusHistoryTable
    queryset = OrderStatusHistory.objects.all()
    filterset_class = OrderStatusHistoryFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "components/tables.html"
        else:
            template_name = "components/tables_full.html"

        return template_name


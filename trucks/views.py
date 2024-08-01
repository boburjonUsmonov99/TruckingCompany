from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import TruckRegistration
from .forms import TruckRegistrationForm

class TruckRegistrationListView(ListView):
    model = TruckRegistration
    template_name = 'trucks/trucks.html'
    context_object_name = 'trucks'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(vin__icontains=query) |
                Q(license_plate_number__icontains=query) |
                Q(unit_number__icontains=query)
            )
        return queryset

class TruckRegistrationCreateView(CreateView):
    model = TruckRegistration
    template_name = 'trucks/create_truck.html'
    form_class = TruckRegistrationForm
    success_url = reverse_lazy('truck_registrations_list')

class TruckRegistrationUpdateView(UpdateView):
    model = TruckRegistration
    template_name = 'trucks/update_truck.html'
    form_class = TruckRegistrationForm
    success_url = reverse_lazy('truck_registrations_list')

class TruckRegistrationDeleteView(DeleteView):
    model = TruckRegistration
    template_name = 'trucks/delete_truck.html'
    success_url = reverse_lazy('truck_registrations_list')

class TruckRegistrationDetailView(DetailView):
    model = TruckRegistration
    template_name = 'trucks/retrieve_truck.html'
    context_object_name = 'truck'

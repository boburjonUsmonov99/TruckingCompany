from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q  # Import Q for complex queries
from django.urls import reverse_lazy

from .forms import DriverForm
from .models import Driver



class DriverListView(ListView):
    model = Driver
    template_name = 'drivers/drivers.html'
    context_object_name = 'drivers'

    def get_queryset(self):
        # Call the base implementation first to get a queryset
        queryset = super().get_queryset()

        # Get the search query from the URL, if it exists
        query = self.request.GET.get('search')

        if query:
            # Filter the queryset based on the number or related name fields containing the query string
            queryset = queryset.filter(
                Q(phone_number__icontains=query) |
                Q(first_name__icontains=query) |
                Q(driver_role__icontains=query) |
                Q(employment_status__icontains=query) |
                Q(last_name__icontains=query)
            )

        # Return the final queryset
        return queryset


# Create
class DriverCreateView(CreateView):
    model = Driver
    template_name = 'drivers/create_driver.html'
    form_class = DriverForm
    context_object_name = 'DriverForm'
    success_url = reverse_lazy('drivers_list')  # Redirect to list view after creating

    def form_valid(self, form):
        return super().form_valid(form)

# Retrieve
class DriverRetrieveView(DetailView):
    model = Driver
    template_name = 'drivers/retrieve_driver.html'
    context_object_name = 'driver'


# Retrieve
class DriverUpdateView(UpdateView):
    model = Driver
    template_name = 'drivers/update_driver.html'
    context_object_name = 'DriverForm'
    form_class = DriverForm
    success_url = reverse_lazy('drivers_list')  # Redirect to list view after creating

# Retrieve
class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'drivers/delete_driver.html'  # Updated template
    context_object_name = 'driver'
    success_url = reverse_lazy('drivers_list')





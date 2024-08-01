from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Transponder, TransponderNameList
from .forms import TransponderForm, TransponderNameForm

class TransponderListView(ListView):
    model = Transponder
    template_name = 'transponders/transponders.html'
    context_object_name = 'transponders'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(number__icontains=query) |
                Q(name__name__icontains(query)) |
                Q(status__icontains=query)
            )
        return queryset

class TransponderCreateView(CreateView):
    model = Transponder
    template_name = 'transponders/create_transponder.html'
    form_class = TransponderForm
    success_url = reverse_lazy('transponders_list')

class TransponderUpdateView(UpdateView):
    model = Transponder
    template_name = 'transponders/update_transponder.html'
    form_class = TransponderForm
    success_url = reverse_lazy('transponders_list')

class TransponderDeleteView(DeleteView):
    model = Transponder
    template_name = 'transponders/delete_transponder.html'
    success_url = reverse_lazy('transponders_list')

class TransponderDetailView(DetailView):
    model = Transponder
    template_name = 'transponders/retrieve_transponder.html'
    context_object_name = 'transponder'

# TransponderNameList Views
class TransponderNameListView(ListView):
    model = TransponderNameList
    template_name = 'transponders/transponder_names.html'
    context_object_name = 'transponder_names'

class TransponderNameCreateView(CreateView):
    model = TransponderNameList
    template_name = 'transponders/create_transponder_name.html'
    form_class = TransponderNameForm
    success_url = reverse_lazy('transponder_names_list')

class TransponderNameUpdateView(UpdateView):
    model = TransponderNameList
    template_name = 'transponders/update_transponder_name.html'
    form_class = TransponderNameForm
    success_url = reverse_lazy('transponder_names_list')

class TransponderNameDeleteView(DeleteView):
    model = TransponderNameList
    template_name = 'transponders/delete_transponder_name.html'
    success_url = reverse_lazy('transponder_names_list')

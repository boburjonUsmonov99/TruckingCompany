from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import FuelCard, FuelCardName
from .forms import FuelCardForm, FuelCardNameForm


class FuelCardListView(ListView):
    model = FuelCard
    template_name = 'fuel_cards/fuel_cards.html'
    context_object_name = 'fuel_cards'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(
                Q(number__icontains=query) |
                Q(status__icontains=query) |
                Q(name__name__icontains=query)
            )
        return queryset

class FuelCardCreateView(CreateView):
    model = FuelCard
    template_name = 'fuel_cards/create_fuel_card.html'
    form_class = FuelCardForm
    success_url = reverse_lazy('fuel_card_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['name'].queryset = FuelCardName.objects.all()
        return form

class FuelCardUpdateView(UpdateView):
    model = FuelCard
    template_name = 'fuel_cards/update_fuel_card.html'
    form_class = FuelCardForm
    success_url = reverse_lazy('fuel_card_list')

class FuelCardDeleteView(DeleteView):
    model = FuelCard
    success_url = reverse_lazy('fuel_card_list')

class FuelCardDetailView(DetailView):
    model = FuelCard
    template_name = 'fuel_cards/retrieve_fuel_card.html'
    context_object_name = 'fuel_card'

class FuelCardNameListView(ListView):
    model = FuelCardName
    template_name = 'fuel_cards/fuel_card_names.html'
    context_object_name = 'fuel_card_names'

class FuelCardNameCreateView(CreateView):
    model = FuelCardName
    template_name = 'fuel_cards/create_fuel_card_name.html'
    form_class = FuelCardNameForm
    success_url = reverse_lazy('fuel_card_names_list')

class FuelCardNameUpdateView(UpdateView):
    model = FuelCardName
    template_name = 'fuel_cards/update_fuel_card_name.html'
    form_class = FuelCardNameForm
    success_url = reverse_lazy('fuel_card_names_list')

class FuelCardNameDeleteView(DeleteView):
    model = FuelCardName
    template_name = 'fuel_cards/delete_fuel_card_name.html'
    success_url = reverse_lazy('fuel_card_names_list')

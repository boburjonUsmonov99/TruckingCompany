from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Trip
from .forms import TripForm, TripLocationFormSet

class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'

class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'

class TripCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TripForm()
        formset = TripLocationFormSet(instance=Trip())
        return render(request, 'trips/trip_form.html', {'form': form, 'formset': formset})

    def post(self, request, *args, **kwargs):
        form = TripForm(request.POST)
        formset = TripLocationFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            trip = form.save()
            formset.instance = trip
            formset.save()
            return redirect('trip_list')
        return render(request, 'trips/trip_form.html', {'form': form, 'formset': formset})

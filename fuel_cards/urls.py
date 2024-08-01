from django.urls import path
from .views import (
    FuelCardListView, FuelCardCreateView, FuelCardUpdateView, FuelCardDeleteView, FuelCardDetailView,
    FuelCardNameListView, FuelCardNameCreateView, FuelCardNameUpdateView, FuelCardNameDeleteView
)

urlpatterns = [
    path('', FuelCardListView.as_view(), name='fuel_cards_list'),
    path('new/', FuelCardCreateView.as_view(), name='fuel_card_create'),
    path('<int:pk>/edit/', FuelCardUpdateView.as_view(), name='fuel_card_edit'),
    path('<int:pk>/delete/', FuelCardDeleteView.as_view(), name='fuel_card_delete'),
    path('<int:pk>/', FuelCardDetailView.as_view(), name='fuel_card_detail'),

    path('names/', FuelCardNameListView.as_view(), name='fuel_card_names_list'),
    path('names/new/', FuelCardNameCreateView.as_view(), name='fuel_card_name_create'),
    path('names/<int:pk>/edit/', FuelCardNameUpdateView.as_view(), name='fuel_card_name_edit'),
    path('names/<int:pk>/delete/', FuelCardNameDeleteView.as_view(), name='fuel_card_name_delete'),
]

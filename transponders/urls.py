from django.urls import path
from .views import (
    TransponderListView, TransponderCreateView, TransponderUpdateView, TransponderDeleteView, TransponderDetailView,
    TransponderNameListView, TransponderNameCreateView, TransponderNameUpdateView, TransponderNameDeleteView
)

urlpatterns = [
    path('', TransponderListView.as_view(), name='transponders_list'),
    path('new/', TransponderCreateView.as_view(), name='transponder_create'),
    path('<int:pk>/edit/', TransponderUpdateView.as_view(), name='transponder_edit'),
    path('<int:pk>/delete/', TransponderDeleteView.as_view(), name='transponder_delete'),
    path('<int:pk>/', TransponderDetailView.as_view(), name='transponder_detail'),

    path('names/', TransponderNameListView.as_view(), name='transponder_names_list'),
    path('names/new/', TransponderNameCreateView.as_view(), name='transponder_name_create'),
    path('names/<int:pk>/edit/', TransponderNameUpdateView.as_view(), name='transponder_name_edit'),
    path('names/<int:pk>/delete/', TransponderNameDeleteView.as_view(), name='transponder_name_delete'),
]

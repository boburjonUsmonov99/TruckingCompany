from django.urls import path
from .views import (
    TruckRegistrationListView, TruckRegistrationCreateView, TruckRegistrationUpdateView,
    TruckRegistrationDeleteView, TruckRegistrationDetailView
)

urlpatterns = [
    path('', TruckRegistrationListView.as_view(), name='truck_registrations_list'),
    path('new/', TruckRegistrationCreateView.as_view(), name='truck_registration_create'),
    path('<int:pk>/edit/', TruckRegistrationUpdateView.as_view(), name='truck_registration_edit'),
    path('<int:pk>/delete/', TruckRegistrationDeleteView.as_view(), name='truck_registration_delete'),
    path('<int:pk>/', TruckRegistrationDetailView.as_view(), name='truck_registration_detail'),
]

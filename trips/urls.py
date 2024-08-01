from django.urls import path
from .views import TripListView, TripDetailView, TripCreateView

urlpatterns = [
    path('', TripListView.as_view(), name='trip_list'),
    path('trip/new/', TripCreateView.as_view(), name='trip_create'),
    path('trip/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
]

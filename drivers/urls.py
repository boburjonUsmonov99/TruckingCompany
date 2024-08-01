from django.urls import path
from .views import DriverListView, DriverCreateView, DriverRetrieveView, DriverUpdateView, DriverDeleteView

urlpatterns = [
    path('', DriverListView.as_view(), name='drivers_list'),
    path('new/', DriverCreateView.as_view(), name='driver_create'),
    path('<int:pk>/', DriverRetrieveView.as_view(), name='driver_retrieve'),
    path('<int:pk>/edit/', DriverUpdateView.as_view(), name='driver_update'),
    path('<int:pk>/delete/', DriverDeleteView.as_view(), name='driver_delete'),
]

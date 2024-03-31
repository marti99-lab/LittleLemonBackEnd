from django.urls import path
from LittleLemonAPI import views
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-items'),
]

from rest_framework import viewsets
from .models import Booking
from .serializers import bookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
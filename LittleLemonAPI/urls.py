from django.urls import path
from restaurant import views


urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('bookings/<int:pk>/', views.BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
]
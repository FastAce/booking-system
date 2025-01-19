from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page
    path("services/", views.services_list, name="services_list"),  # List of services
    path("book/", views.book_service, name="book_service"),  # Booking form
    path("my-bookings/", views.user_bookings, name="user_bookings"),  # User bookings
    path("manage-time-slots/", views.manage_time_slots, name="manage_time_slots"),  # Manage time slots
]

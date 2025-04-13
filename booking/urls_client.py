from django.urls import path
from . import views_client

app_name = "client"

urlpatterns = [
    path("book/", views_client.book_service, name="book_service"),
    path("my-bookings/", views_client.user_bookings, name="user_bookings"),
]


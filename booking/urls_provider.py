from django.urls import path
from . import views_provider

app_name = "provider"

urlpatterns = [
    path("services/", views_provider.services_list, name="services_list"),
    path("manage-time-slots/", views_provider.manage_time_slots, name="manage_time_slots"),
    path("time-slots-json/", views_provider.time_slots_json, name="time_slots_json"),
]


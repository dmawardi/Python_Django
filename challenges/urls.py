from django.urls import path
from . import views

# List of url patterns
urlpatterns = [
    path("", views.index),
    # Uses path function to create path of /january and uses views.index to resolve response
    # path("january", views.january),
    # path("february", views.february),
    # dynamic path with parameter. Allows for type casting
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="str-monthly-challenge")


]

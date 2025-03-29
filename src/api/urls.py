from django.urls import path

from api import views

urlpatterns = [
    path("health/", views.APIHealthView.as_view(), name="api-health"),
]

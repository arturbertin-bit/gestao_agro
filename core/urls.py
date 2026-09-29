from django.urls import path

from areas.urls import app_name
from . import views

urlpatterns = [
    path("", views.index_view, name="index")
]

app_name = "core"
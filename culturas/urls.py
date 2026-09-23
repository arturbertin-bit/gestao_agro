from django.contrib import admin
from django.urls import path

from culturas.views import cultures_list_view
urlpatterns = [
    path("culturas/", cultures_list_view, name="culturas"),
]

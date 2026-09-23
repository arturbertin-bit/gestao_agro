from django.contrib import admin
from django.urls import path, include

from areas.views import areas_list_view

urlpatterns = [
    path("/areas", areas_list_view, name="areas_list"),

]

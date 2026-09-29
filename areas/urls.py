from django.urls import path

from . import views

urlpatterns = [
    path("", views.AreasList.as_view(), name="areas_list"),
    path("create/", views.create_area_view, name="create_area")
]

app_name = "areas"
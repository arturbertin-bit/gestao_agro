from django.urls import path

from . import views

urlpatterns = [
    path("", views.AreasList.as_view(), name="areas_list"),
    path("create/", views.create_area, name="create_area"),
    path("<int:pk>", views.AreaDetailView.as_view(), name="area_detail"),
    path("<int:pk>/edit/", views.AreaUpdateView.as_view(), name="area_update")
]

app_name = "areas"
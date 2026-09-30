from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView

from areas.forms import AreasForm
from areas.models import Area


# Create your views here.
class AreasList(generic.ListView):
    model = Area
    context_object_name = "areas"
    template_name = "areas/areas_list.html"


class AreaDetailView(generic.DetailView):
    model = Area
    context_object_name = "area"
    template_name = "areas/area_detail.html"


def create_area(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = AreasForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("areas:areas_list")
            )
    else:
        form = AreasForm()

    return render(
            request,
            "areas/area_form.html",
            {"form": form}
    )

class AreaUpdateView(UpdateView):
    model = Area
    form_class = AreasForm
    template_name = "areas/area_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "areas:area_detail",
            kwargs={"pk": self.object.pk}
        )

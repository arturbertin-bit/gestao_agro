from difflib import context_diff

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse

from areas.models import Area


# Create your views here.
class AreasList(ListView):
    model = Area
    context_object_name = "areas"
    template_name = "areas/areas_list.html"


def create_area_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "areas/area_form.html")

    if request.method == "POST":
        nome = request.POST.get("nome")
        tamanho = request.POST.get("tamanho")

        if nome and tamanho:
            Area.objects.create(nome=nome, tamanho=tamanho)
            return HttpResponseRedirect(reverse("areas:areas_list"))

        context = {
            "error": "Preencha todos os campos"
        }

        return render(request, "areas/area_form.html")
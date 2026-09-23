from django.http import HttpRequest
from django.shortcuts import render

from culturas.models import Cultura


# Create your views here.
def cultures_list_view(request: HttpRequest) -> HttpResponse:
    culturas = Cultura.objects.all()
    context = {'culturas': culturas}
    return render(request, "culturas/culturas.html", context)
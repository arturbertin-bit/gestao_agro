from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def areas_list_view(request: HttpRequest) -> HttpResponse:

    return render(request, 'areas/areas.html')

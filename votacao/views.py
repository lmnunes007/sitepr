from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Viva DIAM. Esta é a página de entrada da app votacão.")

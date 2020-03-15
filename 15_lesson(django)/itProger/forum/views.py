from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Forum(request):
    return HttpResponse("<h1>Привет Веталь!!!!!</h1>")

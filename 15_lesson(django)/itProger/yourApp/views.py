from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def yourApp(request):
    return HttpResponse("<h1>Hello!!!</h1>")

def some(request):
    return HttpResponse("<h1>Привет мир!</h1>")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = {
        'title':'Simpy'
    }
    # return HttpResponse("<h1>Main Page!!!</h1>")
    return render(request, 'simpy/home.html',data)

def uslugi(request):
    return render(request, 'simpy/uslugi.html')

def contacts(request):
    return render(request, 'simpy/contacts.html')

def about(request):
    return render(request, 'simpy/about.html')

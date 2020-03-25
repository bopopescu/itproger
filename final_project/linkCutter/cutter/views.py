from django.shortcuts import render


def home_page(request):
    return render(request, 'cutter/home.html', {'title': 'Домашняя страница'})

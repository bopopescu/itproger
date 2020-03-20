from django.shortcuts import render
from .models import News
from .models import Article

# Create your views here.

news = [
    {
        'title': 'Наша первая запись',
        'text': 'Просто большой текст для 1 записи',
        'date': '1 января 2020',
        'author': "Виталий"
    },
    {
        'title': 'Наша вторая запись',
        'text': 'Просто большой текст для 2 записи',
        'date': '15 января 2020',
        'author': "джон"
    },
    {
        'title': 'Наша 3 запись',
        'text': 'Просто большой текст для 3 записи',
        'date': '15 января 2020',
        'author': ""
    }
]


def home(request):
    data = {
        'news': News.objects.all(),
        'title': "Главная страница блога"
    }
    return render(request, 'blog/home.html', data)


def contacts(request):
    return render(request, "blog/contacts.html", {'title': 'Страничка про нас!'})


def practice(request):
    data = {
        "title": 'Практика',
        'hello_text': 'Привет мир',
        'id': 'practice'
    }
    return render(request, "blog/practice.html", data)


def lessons(request):
    data = {
        "title": 'Lessons',
        'hello_text': 'Привет Lessons',
    }
    return render(request, 'blog/lessons.html', data)


def about(request):
    data = {
        "title": 'About',
        'hello_text2': 'Привет About'
    }
    return render(request, 'blog/about.html', data)

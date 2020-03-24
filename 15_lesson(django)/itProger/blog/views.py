from django.shortcuts import render
from .models import News
from .models import Article
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']

    def get_context_data(self, object_list=None, **kwargs):
        ctx = super(ShowNewsView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница блога'
        return ctx


class NewsDetailView(DetailView):  # blog/news_detail.html
    model = News

    # context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        return ctx


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News

    fields = ['title', 'text']  # , 'date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News

    fields = ['title', 'text']  # , 'date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        else:
            return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True
        else:
            return False

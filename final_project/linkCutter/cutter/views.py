from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Url


def home_page(request):
    return render(request, 'cutter/home.html', {'title': 'Домашняя страница'})


def about(request):
    return render(request, 'cutter/about.html', {'title': 'Про нас'})


def hrefs(request):
    return render(request, 'cutter/hrefs.html', {'title': 'Создание ссылок'})


class HrefCreateView(LoginRequiredMixin, CreateView):
    model = Url
    template_name = 'cutter/hrefs.html'

    fields = ['url', 'url_name']

    #

    def get_context_data(self, object_list=None, **kwargs):
        filter_object = Url.objects.filter(user=self.request.user)
        ctx = super(HrefCreateView, self).get_context_data(**kwargs)
        ctx['title'] = 'Cсылки'
        ctx['users_urls'] = list(filter_object)
        return ctx

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        return super().form_valid(form)

from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import News


class HomePageView(TemplateView):
    template_name = "application/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.latest('id')
        return context


class NewsPageView(ListView):
    model = News
    template_name = 'application/news.html'
    context_object_name = 'news_list'
    paginate_by = 2  # Количество новостей на странице
    ordering = ['-id']  # Сортировка по id публикации

    def get_context_data(self):
        context = super().get_context_data()
        context["main_news"] = context["news_list"][0]
        if len(context["news_list"]) >= 2:
            context["news_list"] = context["news_list"][1::]
        else:
            context["news_list"] = []
        return context


class SpecificNewsView(DetailView):
    model = News
    template_name = 'application/specific_news.html'
    context_object_name = 'news'
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import News, Products
from .context import DEVELOPERS

class HomePageView(TemplateView):
    template_name = "application/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.latest('id')
        return context


class WorkersPageView(TemplateView):
    template_name = "application/developers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["developers"] = DEVELOPERS
        return context


class NewsPageView(ListView):
    model = News
    template_name = 'application/news.html'
    context_object_name = 'news_list'
    paginate_by = 5  # Количество новостей на странице
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


class ProductsListView(ListView):
    model = Products
    template_name = "application/products.html"
    context_object_name = "products"
    paginate_by = 2


    def get_context_data(self):
        context = super().get_context_data()
        current_path = self.request.path

        if current_path == "/products/":
            context["is_products"] = True
        else:
            context["is_products"] = False

        return context

    def get_queryset(self,):
        current_path = self.request.path
        if current_path == "/products/":
            return self.model.objects.filter(services="Товары", is_moderated=True)
        return self.model.objects.filter(services="Услуги", is_moderated=True)

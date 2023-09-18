from django.urls import path

from .views import (
    HomePageView, NewsPageView, 
    SpecificNewsView, ProductsListView,
    WorkersPageView,
)
urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path('news/', NewsPageView.as_view(), name="news_page"),
    path("news/<int:pk>/", SpecificNewsView.as_view(), name='specific_news'),

    path("products/", ProductsListView.as_view(), name='products_list'),
    path("services/", ProductsListView.as_view(), name='services_list'),

    path("developers/", WorkersPageView.as_view(), name='developers'),
]
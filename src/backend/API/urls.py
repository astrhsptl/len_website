from django.urls import path, include

from .views import ProductCreateAPIView


urlpatterns = [
    path("product/create/", ProductCreateAPIView.as_view(), name="product_create_api"),
]
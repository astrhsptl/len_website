from django.urls import path, include

from .views import ProductCreateAPIView, UserUpdateAPIView


urlpatterns = [
    path("product/create/", ProductCreateAPIView.as_view(), name="product_create_api"),
    path("user/update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update_api"),
    
]
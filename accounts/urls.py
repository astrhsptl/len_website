from django.urls import path, include

from .views import UserListView, UserDetailView, UserProductsListView


urlpatterns = [
    path("", include("allauth.urls")),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/products/", UserProductsListView.as_view(), name="user_detail"),
    path("list/", UserListView.as_view(), name="user_list"),
]
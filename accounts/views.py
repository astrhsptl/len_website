from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

from .models import CustomUser 
from pages.models import Products 


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "account/contactuser/user_detail.html"
    context_object_name = "user_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products.objects.filter(user=context["user_object"])
        context["current_user"] = self.request.user
        return context

class UserListView(ListView):
    model = CustomUser
    queryset = CustomUser.objects.filter(is_staff=False)
    template_name = "account/contactuser/user_list.html"
    context_object_name = "products"

class UserProductsListView(ListView):
    model = Products
    template_name = "account/contactuser/user_detail_products.html"
    context_object_name = "products"

    def get(self, request, pk):
        return super().get(request)

    def get_queryset(self,):
        service = self.request.GET.get('service')
        if service == "" or service == None:
            return self.model.objects.filter(services="Товары", user__id=self.kwargs["pk"])
        return self.model.objects.filter(services=service, user__id=self.kwargs["pk"])
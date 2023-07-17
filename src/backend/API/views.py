from copy import deepcopy
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status

from pages.models import Products
from accounts.models import CustomUser
from .serializers import ProuctSerializer, UserSerializer

class ProductCreateAPIView(CreateAPIView):
    model = Products
    serializer_class = ProuctSerializer
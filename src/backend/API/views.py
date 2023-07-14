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

    # def post(self, request, *args, **kwargs):
    #     try:
    #         total_data = self.serializer_class(request.data).data
    #         print(dir(request))
    #         total_data["user"] = CustomUser.objects.get(pk=total_data["user_id"])
    #         total_data.pop('user_id')
    #         Products.objects.create(**total_data).save()
    #         return Response({"detail": "Successful"}, status=status.HTTP_201_CREATED)
    #     except:
    #         return Response({"detail": "Data error"}, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(UpdateAPIView):
    model = CustomUser
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
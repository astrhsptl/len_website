from rest_framework.serializers import ModelSerializer, IntegerField, ImageField

from pages.models import Products
from accounts.models import CustomUser


class ProuctSerializer(ModelSerializer):
    # user_id = IntegerField()
    image = ImageField(required=False)
    class Meta:
        model = Products
        fields = ('title', 'price', 'city', 'services', 'image', 'user',)

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'middle_name', 'taxpayer',)
from rest_framework.serializers import ModelSerializer, IntegerField

from pages.models import Products


class ProuctSerializer(ModelSerializer):
    user_id = IntegerField()
    class Meta:
        model = Products
        fields = ('title', 'price', 'city', 'services', 'user_id',)
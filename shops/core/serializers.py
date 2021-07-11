from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import City, Street, Shop


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name'
        )


class StreetSerializer(ModelSerializer):
    class Meta:
        model = Street
        fields = (
            'id',
            'name'
        )


class ShopSerializer(ModelSerializer):
    city_name = serializers.CharField(source='city.name', max_length=255, read_only=True)
    street_name = serializers.CharField(source='street.name', max_length=255, read_only=True)

    class Meta:
        model = Shop
        fields = (
            # create fields
            'city',
            'street',
            # get fields
            'city_name',
            'street_name',
            # common fields
            'name',
            'address_number',
            'open_time',
            'closing_time',
        )
        extra_kwargs = {
            'city': {'write_only': True},
            'street': {'write_only': True},
        }

from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from core.filters import ShopFilter
from core.models import City, Street, Shop
from core.serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityListApiView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class StreetListApiView(ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs['city_id'])


class ShopApiView(ListCreateAPIView):
    queryset = Shop.objects.select_related('city').select_related('street').all()
    serializer_class = ShopSerializer
    filterset_class = ShopFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'id': serializer.instance.id}, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

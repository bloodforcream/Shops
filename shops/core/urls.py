from django.urls import path

from core.views import CityListApiView, StreetListApiView, ShopApiView

urlpatterns = [
    path('city/', CityListApiView.as_view(), name='city-list'),
    path('city/<int:city_id>/street/', StreetListApiView.as_view(), name='street-list'),
    path('shop/', ShopApiView.as_view(), name='shop-list-create'),
]

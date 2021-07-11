from django.db import models
from rest_framework.exceptions import ValidationError


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='название города')

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=255, verbose_name='название улицы')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='streets',
                             verbose_name='относящийся город')

    def __str__(self):
        return f'{self.name} - {self.city.name}'


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='название магазина')
    address_number = models.CharField(max_length=10, verbose_name='номер дома')

    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='shops',
                             verbose_name='относящийся город')
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True, related_name='shops',
                               verbose_name='относящиеся улица')

    open_time = models.TimeField(verbose_name='время открытия магазина')
    closing_time = models.TimeField(verbose_name='время закрытия магазина')

    def clean(self):
        #  проверяем относится ли указанная улица к указанному городу
        if self.street.city != self.city:
            raise ValidationError(f'{self.city.name} doesn\'t have {self.street.name} street')

    def save(self, **kwargs):
        self.clean()
        return super(Shop, self).save(**kwargs)

    def __str__(self):
        return f'{self.name} - {self.city.name} - {self.street.name}'

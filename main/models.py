from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import sys, os
sys.path.append(os.path.abspath('../accounts.models'))
from accounts.models import User
from django.urls import reverse


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile = PhoneNumberField(null=False, blank=False)
    region = models.CharField('Регион', max_length=50, default=None)
    city = models.CharField('Город', max_length=50)
    street = models.CharField('Улица', max_length=50)
    house = models.CharField('Дом', max_length=20)
    date = models.DateField(blank=True, null=True)
    sneakers = models.CharField('Кроссовки', max_length=1000, blank=True, null=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
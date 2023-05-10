# from django.conf import settings
from django.db import models
from django.utils import timezone


class RngBaseRecord(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    account_number = models.IntegerField(default=0, null=False, unique=False, verbose_name='Лицевой счёт')
    account_balance = models.FloatField(default=0, null=True, verbose_name='Баланс лицевого счёта')
    service_type_code = models.IntegerField(default=0, null=False, unique=False, verbose_name='Тип услуги')
    meter = models.BooleanField(default=0, null=False, verbose_name='Наличие счётчика')
    meter_readings = models.IntegerField(default=0, null=False, unique=False, verbose_name='Показания счётчика')

    class Meta:
        verbose_name = 'Запись в базе РНГ'
        verbose_name_plural = 'Записи в базе РНГ'

    def __str__(self):
        return f'{self.account_number} / {self.service_type_code} / {self.account_balance}'


class ServicesType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default='', null=False, max_length=254, verbose_name='Название услуги')
    code = models.IntegerField(default=0, null=False, unique=True, verbose_name='Внутренний код услуги')
    rngcode = models.CharField(default='', null=False, unique=True,  max_length=9, verbose_name='Код услуги в РНГ')
    priority = models.IntegerField(default=0, null=False, unique=True, verbose_name='Приоритет списания')

    class Meta:
        verbose_name = 'Тип услуги'
        verbose_name_plural = 'Типы услуг'
    def __str__(self):
        return self.name


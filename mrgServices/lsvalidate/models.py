from django.db import models
from django.utils import timezone

class LsRecord(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    # account_number = models.CharField(default='', null=False, max_length=8, verbose_name='Лицевой счёт (8)')
    # account_number_rng = models.CharField(default='', null=False, max_length=12, verbose_name='Лицевой счёт (12)')
    account_number = models.CharField(default='', null=False, unique=True,  max_length=8, verbose_name='Лицевой счёт (8)')
    account_number_rng = models.CharField(default='', null=False, unique=True,  max_length=12, verbose_name='Лицевой счёт (12)')

    class Meta:
        verbose_name = 'Лицевой счёт'
        verbose_name_plural = 'Лицевые счета'

    def __str__(self):
        return f'{self.account_number} / {self.account_number_rng}'
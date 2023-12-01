from django.db import models
from django.utils import timezone
from contracts.validators import validate_file_extension
from contracts.storage import OverwriteStorage
# Create your models here.

def upload_to(instance, filename):
    print(filename)
    return '/'.join(['vdgo', instance.account_number, filename])

class ContractVdgo(models.Model):

    id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(default=timezone.now)

    account_number = models.CharField(default='', null=True, blank=True, unique=False,  max_length=8, verbose_name='Лицевой счёт (8)')
    account_number_rng = models.CharField(default='', blank=True, null=True, unique=False,  max_length=12, verbose_name='Лицевой счёт (12)')
    account_address = models.CharField(default='', blank=True, null=True, unique=False,  max_length=1024, verbose_name='Адрес установки борудования', validators=[validate_file_extension])
    is_izs = models.BooleanField(default=False, verbose_name='ИЖС')

    contract_pdf = models.FileField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='Заполненный PDF')
    contract_pdf_signed = models.FileField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='Подписанный PDF')

    passport_name = models.CharField(default='', blank=True, null=True, unique=False,  max_length=1024, verbose_name='ФИО владельца договора')
    passport_place = models.CharField(default='', blank=True, null=True, unique=False,  max_length=1024, verbose_name='Место рождения')
    passport_birth_date = models.CharField(default='', blank=True, null=True, unique=False,  max_length=30, verbose_name='Дата рождения')
    passport_serial = models.CharField(default='', blank=True, null=True, unique=False,  max_length=5, verbose_name='Серия паспорта')
    passport_number = models.CharField(default='', blank=True, null=True, unique=False,  max_length=6, verbose_name='Номер паспорта')
    passport_issued_date = models.CharField(default='', blank=True, null=True, unique=False,  max_length=30, verbose_name='Дата выдачи')
    passport_issued = models.CharField(default='', blank=True, null=True, unique=False,  max_length=1024, verbose_name='Кем выдан')
    passport_issued_code = models.CharField(default='', blank=True, null=True, unique=False,  max_length=7, verbose_name='Код подразделения')
    passport_address_registration = models.CharField(default='', blank=True, null=True, unique=False,  max_length=1024, verbose_name='Адрес регистрации')

    passport_scan_first = models.ImageField(upload_to =upload_to, storage=OverwriteStorage(), default = None, blank=True, verbose_name='Второй разворот паспорта',)
    passport_scan_second = models.ImageField(upload_to =upload_to, storage=OverwriteStorage(), default = None, blank=True, verbose_name='Страница паспорта с регистрацией',)


    snils_number = models.CharField(default='', blank=True, null=True, unique=False,  max_length=14, verbose_name='Номер снилс')
    snils_first = models.ImageField(upload_to = upload_to, storage=OverwriteStorage(), blank=True, default='', verbose_name='Лицевая сторона снилс',)

    inn_number = models.CharField(default='', blank=True, null=True, unique=False, max_length=14, verbose_name='Номер ИНН')
    inn_first = models.ImageField(upload_to = upload_to, storage=OverwriteStorage(), blank=True, default='', verbose_name='Лицевая сторона ИНН',)


    certificate_first = models.FileField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='ЕГРН сертификат первый',)
    certificate_second = models.FileField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='ЕГРН сертификат второй',)
    certificate_therd = models.ImageField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='ЕГРН сертификат третий',)
    certificate_fourth = models.ImageField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='ЕГРН сертификат четвёртый',)
    certificate_fifth = models.ImageField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='ЕГРН сертификат пятый',)
    certificate_last = models.ImageField(upload_to = upload_to, storage=OverwriteStorage(), default = '', blank=True, verbose_name='ЕГРН сертификат шестой',)

    phone = models.CharField(default='', blank=True, null=True, unique=False,  max_length=16, verbose_name='Телефон')
    email = models.CharField(default='', blank=True, null=True, unique=False,  max_length=1024, verbose_name='Емайл')
    confirm = models.BooleanField(default=False, verbose_name='Согласие с политикой')
    consent = models.BooleanField(default=False, verbose_name='Подтверждение корректности данных')

    sms = models.BooleanField(default=False, verbose_name='СМС')
    is_signed = models.BooleanField(default=False, verbose_name='Получена подпись')

    is_sended = models.BooleanField(default=False, verbose_name='Отправлено в реестр')
    is_error = models.BooleanField(default=False, verbose_name='Ошибка')
    is_finish = models.BooleanField(default=False, verbose_name='Обработка завершена')
    error_text = models.CharField(default='', blank=True, null=True, unique=False,  max_length=1024, verbose_name='Текст ошибки')


    class Meta:
        verbose_name = 'Договор ВДГО'
        verbose_name_plural = 'Договоры на обслуживание ВДГО'

    def __str__(self):
        return f'{self.account_number} / {self.account_number_rng}'
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from django.conf import settings

# Register your models here.
from contracts.models import ContractVdgo
# Register your models here.


@admin.register(ContractVdgo)
class ContractVdgoAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            None,
            {
                "fields": [
                        ("account_number", "account_number_rng", "is_izs", "account_address"),
                        ("id", "created_date", "last_update_date", "is_sended", "is_signed", "is_error"),
                        ("error_text"),
                        ("contract_pdf", "contract_pdf_signed"),
                    ],
            },
        ),
        (
            "Паспортные данные",
            {
                "classes": ["collapse"],
                "fields": [
                    ('passport_name',),
                    ('passport_place', 'passport_birth_date', 'passport_serial', 'passport_number', 'passport_issued_date', 'passport_issued','passport_issued_code',),
                    ('passport_address_registration', ),
                    ('passport_scan_first', 'passport_scan_second', ),
                ],
            }
        ),
        (
            "Прочие документы",
            {
                "classes": ["collapse"],
                "fields": [
                    ('snils_number','snils_first',),
                    ('inn_number','inn_first',),
                    'certificate_first',
                    'certificate_second',
                    'certificate_therd',
                    'certificate_fourth',
                    'certificate_fifth',
                    'certificate_last',

                ],
            }
        ),
        (
            "Контакты и согласия",
            {
                "classes": ["collapse"],
                "fields": [
                    'phone',
                    'email',
                    'sms',
                    'confirm',
                    'consent',
                ],
            }
        ),
    ]
    formfield_overrides = {
        models.CharField: {"widget": Textarea},
    }
    list_filter = ('consent', 'is_signed', 'is_sended', 'is_izs', )
    if settings.DEBUG == True:
        readonly_fields = (
            'id',
            'created_date',
            'account_number',
            'account_number_rng',
            'last_update_date',
            'account_address',
            'is_izs',
            'contract_pdf',
            'contract_pdf_signed',
            'passport_name',
            'passport_place',
            'passport_birth_date',
            'passport_serial',
            'passport_number',
            'passport_issued_date',
            'passport_issued',
            'passport_issued_code',
            'passport_address_registration',
            'passport_scan_first',
            'passport_scan_second',
            'snils_number',
            'certificate_first',
            'certificate_second',
            'certificate_therd',
            'certificate_fourth',
            'certificate_fifth',
            'certificate_last',
            'phone',
            'email',
            'confirm',
            'consent',
            'sms',
            'is_signed',
            'is_sended',
            )
    else:
        readonly_fields = ('id', 'created_date', 'account_number', 'account_number_rng', 'last_update_date', "account_address")

    list_display = [ 'account_number', 'account_number_rng', 'is_izs', 'last_update_date', 'consent', 'is_signed', 'is_sended' ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
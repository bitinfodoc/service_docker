from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

# Register your models here.
from contracts.models import ContractVdgo
# Register your models here.


@admin.register(ContractVdgo)
class ContractVdgoAdmin(admin.ModelAdmin):
    # fields = (
    #             ('id', 'created_date'),
    #             ('account_number', 'account_number_rng', ),
    #             'passport_name',
    #             ('passport_place', 'passport_birth_date', 'passport_serial', 'passport_number', 'passport_issued_date', 'passport_issued','passport_issued_code',),
    #             ('passport_address_registration', ),

    #         )
    fieldsets = [
        (
            None,
            {
                "fields": [("id", "created_date", "account_number", "account_number_rng")],
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
                    'confirm',
                    'consent',
                ],
            }
        ),
    ]
    formfield_overrides = {
        models.CharField: {"widget": Textarea},
    }
    readonly_fields = ('id', 'created_date', )
    list_display = [ 'id', 'last_update_date', 'account_number', 'account_number_rng', ]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
from django.contrib import admin
from rng_base.models import RngBaseRecord, ServicesType


@admin.register(RngBaseRecord)
class RngBaseRecordAdmin(admin.ModelAdmin):
    fields = (('id', 'created_date'), ('account_number', 'account_balance', 'service_type_code'), ('meter_readings', 'meter') )
    readonly_fields = ('id', 'created_date', 'account_number', 'account_balance', 'service_type_code', 'meter_readings', 'meter' )
    list_display = [ 'id', 'created_date', 'account_number', 'account_balance', 'service_type_code', 'meter_readings', 'meter' ]

@admin.register(ServicesType)
class ServicesTypeAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name', 'code', 'rngcode', 'priority' ]
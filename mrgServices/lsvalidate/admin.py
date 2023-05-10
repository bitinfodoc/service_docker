from django.contrib import admin
from lsvalidate.models import LsRecord
# Register your models here.


@admin.register(LsRecord)
class LsRecordAdmin(admin.ModelAdmin):
    fields = (('id', 'created_date'), ('account_number', 'account_number_rng', ))
    # readonly_fields = ('id', 'created_date', 'account_number', 'account_number_rng', )
    readonly_fields = ('id', 'created_date', )
    list_display = [ 'id', 'created_date', 'account_number', 'account_number_rng', ]
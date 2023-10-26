# Generated by Django 4.1.7 on 2023-10-26 21:31

import contracts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0007_contractvdgo_confirm_contractvdgo_consent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractvdgo',
            name='certificate_fifth',
            field=models.ImageField(blank=True, default='', upload_to=contracts.models.upload_to, verbose_name='ЕГРН сертификат пятый'),
        ),
        migrations.AddField(
            model_name='contractvdgo',
            name='certificate_first',
            field=models.ImageField(blank=True, default='', upload_to=contracts.models.upload_to, verbose_name='ЕГРН сертификат первый'),
        ),
        migrations.AddField(
            model_name='contractvdgo',
            name='certificate_fourth',
            field=models.ImageField(blank=True, default='', upload_to=contracts.models.upload_to, verbose_name='ЕГРН сертификат четвёртый'),
        ),
        migrations.AddField(
            model_name='contractvdgo',
            name='certificate_last',
            field=models.ImageField(blank=True, default='', upload_to=contracts.models.upload_to, verbose_name='ЕГРН сертификат шестой'),
        ),
        migrations.AddField(
            model_name='contractvdgo',
            name='certificate_second',
            field=models.ImageField(blank=True, default='', upload_to=contracts.models.upload_to, verbose_name='ЕГРН сертификат второй'),
        ),
        migrations.AddField(
            model_name='contractvdgo',
            name='certificate_therd',
            field=models.ImageField(blank=True, default='', upload_to=contracts.models.upload_to, verbose_name='ЕГРН сертификат третий'),
        ),
    ]
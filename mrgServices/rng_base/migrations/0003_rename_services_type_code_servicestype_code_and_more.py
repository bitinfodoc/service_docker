# Generated by Django 4.1.7 on 2023-03-01 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rng_base', '0002_alter_rngbaserecord_id_alter_servicestype_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicestype',
            old_name='services_type_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='servicestype',
            old_name='services_type_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='servicestype',
            old_name='services_type_priority',
            new_name='priority',
        ),
        migrations.RenameField(
            model_name='servicestype',
            old_name='services_type_rngcode',
            new_name='rngcode',
        ),
    ]

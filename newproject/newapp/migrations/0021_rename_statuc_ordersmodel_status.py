# Generated by Django 3.2.5 on 2021-07-27 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0020_ordersmodel_statuc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordersmodel',
            old_name='statuc',
            new_name='status',
        ),
    ]

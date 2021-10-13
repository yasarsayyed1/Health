# Generated by Django 3.2.5 on 2021-07-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0015_nursingmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roomservicemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('male', 'male'), ('famale', 'female')], max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]

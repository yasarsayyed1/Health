# Generated by Django 3.2.5 on 2021-07-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulancemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=50)),
                ('patientage', models.CharField(max_length=50)),
                ('contactnumber', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=30)),
                ('diseace', models.CharField(max_length=40)),
            ],
        ),
    ]

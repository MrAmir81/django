# Generated by Django 5.1.5 on 2025-02-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=250, verbose_name='آدرس الکترونیکی')),
                ('phone', models.CharField(max_length=20, verbose_name='تلفن')),
                ('number', models.IntegerField(verbose_name='تعداد')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('time', models.TimeField(verbose_name='ساعت')),
            ],
        ),
    ]

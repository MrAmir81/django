# Generated by Django 5.1.5 on 2025-02-06 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('B', 'صبحانه'), ('D', 'نوشیدنی'), ('DI', 'شام'), ('L', 'ناهار')], default='D', max_length=10, verbose_name='نوع غذا'),
        ),
    ]

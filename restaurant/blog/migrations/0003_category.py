# Generated by Django 5.1.5 on 2025-02-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان لاتین')),
                ('published_at', models.DateTimeField(verbose_name='تاریخ انتشار')),
            ],
        ),
    ]

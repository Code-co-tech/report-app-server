# Generated by Django 5.1.2 on 2024-10-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activate_profile',
            field=models.BooleanField(default=False, verbose_name='Активировать профиль'),
        ),
    ]
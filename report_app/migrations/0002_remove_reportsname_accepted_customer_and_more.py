# Generated by Django 5.1.2 on 2024-10-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportsname',
            name='accepted_customer',
        ),
        migrations.RemoveField(
            model_name='reportsname',
            name='constructor_accepted',
        ),
        migrations.RemoveField(
            model_name='reportsname',
            name='expired_admin',
        ),
        migrations.RemoveField(
            model_name='reportsname',
            name='expired_customer',
        ),
        migrations.AddField(
            model_name='reportsname',
            name='status_customer',
            field=models.IntegerField(choices=[(1, 'Отправлено'), (2, 'Принято'), (3, 'Отказ')], default=1, verbose_name='Статус подрядчики'),
        ),
        migrations.AddField(
            model_name='reportsname',
            name='status_user',
            field=models.IntegerField(choices=[(1, 'Отправлено'), (2, 'Принято'), (3, 'Отказ')], default=1, verbose_name='Статус пользователя'),
        ),
    ]

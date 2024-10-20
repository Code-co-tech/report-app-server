# Generated by Django 5.1.2 on 2024-10-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_app', '0002_remove_reportsname_accepted_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportsname',
            name='status',
            field=models.IntegerField(choices=[(1, 'Новый'), (2, 'В обработке'), (3, 'Принят'), (4, 'Отказ')], default=1, verbose_name='Статус администратора'),
        ),
        migrations.AlterField(
            model_name='reportsname',
            name='status_customer',
            field=models.IntegerField(choices=[(1, 'Новый'), (2, 'Отправлено'), (3, 'Принято'), (4, 'Отказ')], default=1, verbose_name='Статус подрядчики'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0010_alter_prescriptions_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptioncontractor',
            name='status',
            field=models.IntegerField(choices=[(1, 'В обработке'), (2, 'Устранено'), (3, 'Просрочено'), (4, 'Новый'), (5, 'Null')], default=1, verbose_name='Статус для подрядчика'),
        ),
        migrations.AlterField(
            model_name='prescriptions',
            name='status',
            field=models.IntegerField(choices=[(1, 'В обработке'), (2, 'Устранено'), (3, 'Просрочено'), (4, 'Новый'), (5, 'Null')], default=1, verbose_name='Статус'),
        ),
    ]
# Generated by Django 5.1.2 on 2024-10-13 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_alter_company_inn_company_alter_company_name_company_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компании', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelTable(
            name='company',
            table='company',
        ),
    ]
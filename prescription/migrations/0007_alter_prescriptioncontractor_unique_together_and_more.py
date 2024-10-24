# Generated by Django 5.1.2 on 2024-10-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0006_remove_prescriptions_contractor_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prescriptioncontractor',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='prescriptions',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Срок устранения'),
        ),
        migrations.RemoveField(
            model_name='prescriptioncontractor',
            name='deadline',
        ),
    ]

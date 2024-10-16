# Generated by Django 5.1.2 on 2024-10-18 08:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_account', '0003_alter_project_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfViolation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Тип нарушения')),
            ],
            options={
                'verbose_name': 'Тип нарушения',
                'verbose_name_plural': 'Тип нарушения',
                'db_table': 'type_of_violation',
            },
        ),
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField(verbose_name='Срок устранения')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('contractor', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Подрядчик')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_account.project', verbose_name='Проект')),
                ('type_violation', models.ManyToManyField(blank=True, to='prescription.typeofviolation', verbose_name='Тип нарушения')),
            ],
            options={
                'verbose_name': 'Предписания',
                'verbose_name_plural': 'Предписания',
                'db_table': 'prescriptions',
            },
        ),
        migrations.CreateModel(
            name='PrescriptionsComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Предписания комментарий')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription_comment', to='prescription.prescriptions')),
            ],
            options={
                'verbose_name': 'Предписания комментарий',
                'verbose_name_plural': 'Предписания комментарий',
                'db_table': 'prescriptions_comment',
            },
        ),
        migrations.CreateModel(
            name='PrescriptionsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='prescriptions_image', verbose_name='Предписания изображение')),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prescription_image', to='prescription.prescriptions')),
            ],
            options={
                'verbose_name': 'Предписания изображение',
                'verbose_name_plural': 'Предписания изображение',
                'db_table': 'prescriptions_image',
            },
        ),
    ]

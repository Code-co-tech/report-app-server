from django.db import models
from authen.models import CustomUser
from admin_account.models import Project


# class Prescription(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.SET_NULL, verbose_name='')
#     customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, verbose_name='')
    


class Bob(models.Model):
    name = models.CharField(max_length=250, verbose_name='Раздел')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "bob"
        verbose_name = "Раздел"
        verbose_name_plural = "Раздел"


class TypeWork(models.Model):
    name = models.CharField(max_length=250, verbose_name='Тип работ')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "type_work"
        verbose_name = "Тип работ"
        verbose_name_plural = "Тип работ"


class ReportsName(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название отчета')
    STATUS_USER = (
        (1, 'Отправлено'),
        (2, 'Принято'),
        (3, 'Отказ'),
        (4, 'Null'),
    )
    status_user = models.IntegerField(choices=STATUS_USER, default=4, verbose_name='Статус пользователя')
    STATUS_CONTR = (
        (1, 'Новый'),
        (2, 'Отправлено'),
        (3, 'Принято'),
        (4, 'Отказ'),
        (5, 'Null'),
    )
    status_contractor = models.IntegerField(choices=STATUS_CONTR, default=5, verbose_name='Статус подрядчики')
    STATUS_CUSTOMER = (
        (1, 'Новый'),
        (2, 'Отправлено'),
        (3, 'Принято'),
        (4, 'Отказ'),
        (5, 'Null'),
    )
    status_customer = models.IntegerField(choices=STATUS_CUSTOMER, default=5, verbose_name='Статус сотрудники')
    STATUS = (
        (1, 'Новый'),
        (2, 'В обработке'),
        (3, 'Принят'),
        (4, 'Отказ'),
        (5, 'Null'),
    )
    status = models.IntegerField(choices=STATUS, default=5, verbose_name='Статус администратора')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='user', verbose_name='Пользователь')
    constructor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='constructor', verbose_name='Подрядчики')
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='customer', verbose_name='Сотрудники')
    admin = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='admin', verbose_name='Администратора')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reports"
        verbose_name = "Отчеты"
        verbose_name_plural = "Отчеты"


class Reports(models.Model):
    reports_name = models.ForeignKey(ReportsName, on_delete=models.CASCADE, null=True, blank=True, related_name='resposts', verbose_name='Название отчета')
    bob = models.ForeignKey(Bob, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Раздел')
    type_work = models.ForeignKey(TypeWork, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Тип работ')
    position = models.CharField(max_length=250, verbose_name='Позиция')
    quantity = models.CharField(max_length=250, verbose_name='Количество')
    frame = models.CharField(max_length=250, verbose_name='Корпус')
    floor = models.CharField(max_length=250, verbose_name='Этаж')
    mark = models.CharField(max_length=250, verbose_name='Отметка')
    axles = models.CharField(max_length=250, verbose_name='Оси')
    premises = models.CharField(max_length=250, verbose_name='Помещение')
    completions = models.CharField(max_length=250, verbose_name='Завершения')
    files = models.FileField(upload_to='reports_file/', null=True, blank=True, verbose_name='Файл отчетов')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reports_1"
        verbose_name = "Отчеты"
        verbose_name_plural = "Отчеты"


class RespostComment(models.Model):
    repost = models.ForeignKey(ReportsName, on_delete=models.CASCADE, null=True, blank=True, related_name='respost_comment', verbose_name='Отчеты')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Отправитель')
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "repost_comment"
        verbose_name = "Комментарий отчетов"
        verbose_name_plural = "Комментарий отчетов"
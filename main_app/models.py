from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Town(models.Model):
    town_name = models.CharField(verbose_name='Город', max_length=128, unique=True)

    def __str__(self):
        return f'{self.town_name}'


class AdressInfo(models.Model):
    town_name = models.ForeignKey(to=Town, on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Улица', max_length=128)

    def __str__(self):
        return f'{self.town_name} {self.address}'


class VipNetInfo(models.Model):
    WINDOWS_7 = 'Windows 7'
    WINDOWS_10 = 'Windows 10'
    ASTRA_LINUX = 'ASTRA_LINUX'

    OS_CHOICES = (
        (WINDOWS_7, 'Windows 7'),
        (WINDOWS_10, 'Windows 10'),
        (ASTRA_LINUX, 'ASTRA_LINUX'),
    )

    pc_name = models.CharField(verbose_name='имя компьютера', max_length=64, unique=True)
    operation_system = models.CharField(choices=OS_CHOICES, verbose_name='Операционная система', max_length=24, default=WINDOWS_7)
    hdd_number = models.CharField(verbose_name='Учетный номер ЖМД', max_length=32, blank=False)
    hdd_serial = models.CharField(verbose_name='Серийный номер ЖМД', max_length=64, blank=False)
    inventory_number = models.CharField(verbose_name='Инвентарный номер', max_length=64, blank=False, unique=True)
    pc_model = models.CharField(verbose_name='Модель ПЭВМ', max_length=64, blank=True)
    pc_mac_address = models.CharField(verbose_name='MAC адрес ПЭВМ', max_length=32)
    kaspersky = models.BooleanField(verbose_name='Начличие антивируса Касперский', default=True)
    vipnet_name = models.CharField(verbose_name='Название VipNet ключа', max_length=64)
    address = models.ForeignKey(to=AdressInfo, on_delete=models.CASCADE)
    office_number = models.PositiveIntegerField(verbose_name='Номер кабинета')
    #user info
    username = models.EmailField(unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=150)
    last_name = models.CharField(verbose_name='Фамилия', max_length=150)
    fathers_name = models.CharField(verbose_name='Отчество', max_length=150)
    division = models.CharField(verbose_name='Подразделение', max_length=150)
    position = models.CharField(verbose_name='Должность', max_length=150)
    created = models.BooleanField(verbose_name='Создан', default=False)


class User(AbstractUser):
    email = models.EmailField(unique=True)

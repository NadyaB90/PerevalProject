from django.contrib.auth.models import User
from django.db import models


class PerevalUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fam = models.CharField(max_length=254, default=None, verbose_name="Фамилия")
    name = models.CharField(max_length=254, default=None, verbose_name="Имя")
    otc = models.CharField(max_length=255, verbose_name="Отчество")
    phone = models.CharField(max_length=64, verbose_name="Номер телефона")
    email = models.EmailField(unique=True, default=None, verbose_name="Эл.почта")

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'


class Coords(models.Model):
    latitude = models.FloatField(max_length=15, verbose_name="Широта")
    longitude = models.FloatField(max_length=15, verbose_name="Долгота")
    height = models.IntegerField(verbose_name="Высота")


class PerevalAdded(models.Model):
    new = 'NEW'
    pending = 'PND'
    accepted = 'ACP'
    rejected = 'RGT'
    STATUS = [
        (new, 'Новая заявка'),
        (pending, 'Заявка на модерации'),
        (accepted, 'Модерация прошла успешно'),
        (rejected, 'Модерация прошла, информация не принята'),
    ]
    beautyTitle = models.CharField(max_length=254)
    title = models.CharField(max_length=254, unique=True)
    other_titles = models.CharField(max_length=254)
    connect = models.TextField(blank=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    user = models.ForeignKey(PerevalUser, on_delete=models.CASCADE, related_name='pereval')
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS, default=new)
    level_spring = models.CharField(max_length=254, blank=True, verbose_name="Сложность весной")
    level_summer = models.CharField(max_length=254, blank=True, verbose_name="Сложность летом")
    level_autumn = models.CharField(max_length=254, blank=True, verbose_name="Сложность осенью")
    level_winter = models.CharField(max_length=254, blank=True, verbose_name="Сложность зимой")

    def __str__(self):
        return f"id: {self.pk}, title:{self.title}"


class PerevalImages(models.Model):
    title = models.CharField(max_length=254, verbose_name="Название")
    img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    date_added = models.DateField(auto_now_add=True, verbose_name="Время добавления")

    def __str__(self):
        return f"id: {self.pk}, title:{self.title}"

    class Meta:
        verbose_name_plural = "Фотографии"


class PerevalAreas(models.Model):
    id_parent = models.IntegerField(null=True)
    title = models.TextField(null=True)

    class Meta:
        db_table = 'pereval_areas'


class SprActivitiesTypes(models.Model):
    title = models.TextField(null=True)

    class Meta:
        db_table = 'spr_activities_types'
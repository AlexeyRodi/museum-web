# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Exhibit(models.Model):
    exhibit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creation_year = models.IntegerField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    room = models.ForeignKey('Museum_Room', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exhibit'
        verbose_name = 'Экспонат'
        verbose_name_plural = 'Экспонаты'


class Exhibit_Exhibition(models.Model):
    exhibit = models.OneToOneField(Exhibit, models.DO_NOTHING, primary_key=True)  # The composite primary key (exhibit_id, exhibition_id) found, that is not supported. The first column is selected.
    exhibition = models.ForeignKey('Exhibition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exhibit_exhibition'
        unique_together = (('exhibit', 'exhibition'),)


class Exhibition(models.Model):
    exhibition_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True)
    responsible_person = models.CharField(max_length=255, blank=True, null=True)
    museum = models.ForeignKey('Museum', models.DO_NOTHING, blank=True, null=True)

    def get_absolute_url(self):
        return '/выставки/'

    class Meta:
        managed = False
        db_table = 'exhibition'
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'


class Exhibition_Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exhibition_category'
        verbose_name = 'Категория выставок'
        verbose_name_plural = 'Категории выставок'


class Exhibition_Exhibition_Category(models.Model):
    exhibition = models.OneToOneField(Exhibition, models.DO_NOTHING, primary_key=True)  # The composite primary key (exhibition_id, category_id) found, that is not supported. The first column is selected.
    category = models.ForeignKey(Exhibition_Category, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exhibition_exhibition_category'
        unique_together = (('exhibition', 'category'),)


class Museum(models.Model):
    museum_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'museum'
        verbose_name = 'Музей'
        verbose_name_plural = 'Музеи'

    def __str__(self):
        return self.name


class Museum_Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    museum = models.ForeignKey(Museum, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'museum_room'
        verbose_name = 'Комната музея'
        verbose_name_plural = 'Комнаты музея'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    password = models.TextField()
    role = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


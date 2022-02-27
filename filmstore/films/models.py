from django.db import models


class Director(models.Model):
    full_name = models.CharField(
        max_length=255, null=False, blank=False, db_column="full_name", verbose_name="Полное имя режиссёра"
    )
    birth_date = models.DateField(null=False, blank=False, db_column="birth_date", verbose_name="Дата рождения")
    age = models.IntegerField(null=False, blank=False, db_column="age", verbose_name="Возраст")
    death_date = models.DateField(
        null=False, blank=False, db_column="death_date", default="9999-12-31", verbose_name="Дата смерти"
    )
    cover = models.FileField(null=True, blank=True, verbose_name="Фото режиссёра")
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.full_name}"


class Genre(models.Model):
    name = models.CharField(
        max_length=255, null=False, blank=False, db_column="name", unique=True, verbose_name="Название жанра"
    )
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=255, db_column="title")
    release_year = models.DateField(max_length=255, null=False, blank=False, db_column="release_year",
                                    verbose_name="Год выхода фильма")
    price = models.DecimalField(
        max_digits=19, decimal_places=2, null=False, blank=False, db_column="price", verbose_name="Цена"
    )
    directors = models.ManyToManyField(Director, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.title}, {self.release_year}"


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models

from users.models import User

from .validators import validate_date

SYMBOLS_LIMIT = 15


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',
                            max_length=256)
    slug = models.SlugField(verbose_name='Метка категории',
                            max_length=50,
                            unique=True,
                            validators=[RegexValidator(r'^[-a-zA-Z0-9_]+$',
                                        message='Недопустимые символы')])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра',
                            max_length=256)
    slug = models.SlugField(verbose_name='Метка жанра',
                            max_length=50,
                            unique=True,
                            validators=[RegexValidator(r'^[-a-zA-Z0-9_]+$',
                                        message='Недопустимые символы')])

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(verbose_name='Название произведения',
                            max_length=200)
    year = models.IntegerField(verbose_name='Дата выхода',
                               validators=[validate_date],
                               default=None)
    description = models.TextField(verbose_name='Описание произведения',
                                   null=True,
                                   blank=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр произведения')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория произведения',
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 null=True)
    rating = models.IntegerField(verbose_name='Рейтинг',
                                 null=True,
                                 default=None)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(Title,
                              verbose_name='Произведение',
                              on_delete=models.CASCADE,
                              related_name='reviews')
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(User,
                               verbose_name='Автор',
                               on_delete=models.CASCADE,
                               related_name='reviews')
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Допустимы значения от 1 до 10'),
            MaxValueValidator(10, 'Допустимы значения от 1 до 10')
        ]
    )
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True,
                                    db_index=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique_review'), ]

    def __str__(self):
        return self.text[:SYMBOLS_LIMIT]


class Comment(models.Model):
    review = models.ForeignKey(Review,
                               verbose_name='Отзыв',
                               on_delete=models.CASCADE,
                               related_name='comments')
    text = models.TextField(verbose_name='Текст', )
    author = models.ForeignKey(User,
                               verbose_name='Пользователь',
                               on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True,
                                    db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']

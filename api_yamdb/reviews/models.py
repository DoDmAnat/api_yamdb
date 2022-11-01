from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = [(ADMIN, 'Administrator'),
             (MODERATOR, 'Moderator'),
             (USER, 'User'), ]

    username = models.CharField(verbose_name='Имя пользователя',
                                max_length=150,
                                null=True,
                                unique=True)
    email = models.EmailField(verbose_name='Адрес почты',
                              unique=True, )
    role = models.CharField(verbose_name='Должность',
                            max_length=50,
                            choices=ROLES,
                            default=USER)
    bio = models.TextField(verbose_name='Биография',
                           null=True,
                           blank=True)

    def is_moderator(self):
        return self.role == self.MODERATOR

    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        # Не уверен что правильно, но как-то так
        constraints = [
            models.CheckConstraint(check=models.Q(username='me'),
                                   name='username_is_not_me')]


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории',
                            max_length=256)
    slug = models.SlugField(verbose_name='Метка категории',
                            max_length=50,
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Genre(models.Model):
    name = models.CharField(verbose_name='Название жанра',
                            max_length=256)
    slug = models.SlugField(verbose_name='Метка жанра',
                            max_length=50,
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']


class Title(models.Model):
    name = models.CharField(verbose_name='Название произведения',
                            max_length=200)
    description = models.TextField(verbose_name='Описание произведения',
                                   null=True,
                                   blank=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр произведения',
                                   through='GenreTitle')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория произведения',
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 null=True)
    rating = models.IntegerField(verbose_name='Рейтинг',
                                 null=True,
                                 default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['name']


class Review(models.Model):
    title = models.ForeignKey(Title,
                              verbose_name='Произведение',
                              on_delete=models.CASCADE,
                              related_name='reviews')
    text = models.TextField(verbose_name='Текст', )
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
        ordering = ['pub_date']
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'],
                                    name='unique_review'), ]


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

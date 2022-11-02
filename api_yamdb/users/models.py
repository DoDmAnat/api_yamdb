from django.contrib.auth.models import AbstractUser
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
        # constraints = [
        # models.CheckConstraint(check=models.Q(username='me'),
        # name='username_is_not_me')]

import secrets
import string
from unittest.util import _MAX_LENGTH

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

LENGTH = 6


def generate_confirmation_code():
    return ''.join(secrets.choice(
        string.ascii_uppercase + string.digits
    ) for x in range(LENGTH))


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

    USERNAME_FIELD = 'username'

    def is_moderator(self):
        return self.role == self.MODERATOR

    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = [
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_username_email'
            )
        ]

    def __str__(self):
        return self.username


class ConfirmationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    code = models.CharField(
        max_length=LENGTH, default=generate_confirmation_code
    )

    def __str__(self):
        return self.code

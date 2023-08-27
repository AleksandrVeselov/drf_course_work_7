from django.contrib.auth.models import AbstractUser
from django.db import models

from spa.models import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    telegram_id = models.CharField(max_length=100, verbose_name='Телеграм ID пользователя', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

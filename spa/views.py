from django.conf import settings
from django.shortcuts import render
from rest_framework import generics

from spa.models import Habit
from spa.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """Класс-представление для отображения списка всех привычек текущего пользователя"""

    serializer_class = HabitSerializer  # Сериализатор
    queryset = Habit.Objects.filter(user=settings.AUTH_USER_MODEL)  # список всех привычек авторизованного пользователя

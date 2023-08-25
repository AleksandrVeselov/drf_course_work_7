from django.contrib import admin

from spa.models import Habit

# Register your models here.

admin.site.register(Habit)  # регистрация модели "привычка" в админ-панели

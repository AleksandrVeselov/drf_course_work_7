from datetime import datetime

from celery import shared_task

from spa.models import Habit


@shared_task
def check_habits():
    """Задача для периодического запуска.
    Поиск привычек, проверка на соответствие текущего времени и времени,
    заложенного в атрибут habit_time модели Привычка и отправки сообщения в телеграмм"""

    current_datetime = datetime.now().replace(second=0, microsecond=0)  # текущая дата/время
    current_time = current_datetime.time().replace(second=0, microsecond=0)  # текущее время без секунд и микросекунд

    habits = Habit.objects.all()  # все привычки

    for habit in habits:

        # время выполнения привычки без секунд и микросекунд
        habit_time = habit.habit_time.replace(second=0, microsecond=0)

        # если время привычки равно текущему времени без учета секунд
        if habit_time == current_time:
            send_telegram_message(habit)

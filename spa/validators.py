from datetime import timedelta

from rest_framework.exceptions import ValidationError

from spa.models import Habit


class ExecutionTimeValidator:
    """Проверка длительности поля execution_time"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        models_dict = dict(value)  # словарь из полей модели
        execution_time = models_dict.get(self.field)  # значение времени выполнения
        if execution_time > timedelta(seconds=120):
            raise ValidationError('Время выполнения привычки не должно превышать 120 секунд')


class RelatedHabitValidation:
    """Проверка наличия у связанной привычки признака is_pleasant"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        award = dict(value).get('award')  # Наличие вознаграждения у привычки
        pleasant_habit = Habit.objects.filter(pk=self.field, is_pleasant=True).exist()

        if award and self.field:
            raise ValidationError('Невозможно одновременно указать связанную привычку и вознаграждение')

        elif not pleasant_habit:
            raise ValidationError('В связанные привычки может попасть привычка с признаком приятной (is_pleasant=True)')


class IsPleasantValidator:
    """У приятной привычки не может быть вознаграждения или связанной привычки"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):

        # если привычка приятная (is_pleasant=True)
        if self.field:
            award = dict(value).get('award')
            related_habit = dict(value).get('related_habit')
            if award or related_habit:
                raise ValidationError(
                    'У приятной привычки (is_pleasant=True) не может быть вознаграждения или связанной привычки')


class PeriodicityValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get('periodicity')

        if periodicity > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')







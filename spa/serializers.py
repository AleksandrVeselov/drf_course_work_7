from rest_framework import serializers

from spa.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор модели Привычка (Habit)"""

    class Meta:
        model = Habit
        fields = '__all__'

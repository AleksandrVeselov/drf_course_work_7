from django.urls import path

from spa.apps import SpaConfig
from spa.views import (HabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView,
                       HabitDeleteAPIView)

appname = SpaConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('public', PublicHabitListAPIView.as_view(), name='public_habit_list'),
    path('create', HabitCreateAPIView.as_view(), name='create_habit'),
    path('update', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('delete', HabitDeleteAPIView.as_view(), name='delete'),
]

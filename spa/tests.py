from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from spa.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование модели привычка"""

    def setUp(self):
        """Подготовка данных перед каждым тестом"""

        # Создание пользователя для тестирования
        self.user = User.objects.create(email='test_user@test.ru',
                                        is_staff=False,
                                        is_superuser=False,
                                        is_active=True)

        self.user.set_password('qwerty')  # Устанавливаем пароль
        self.user.save()  # Сохраняем изменения пользователя в базе данных

        # Запрос токена для авторизации
        response = self.client.post('/users/token/', data={'email': self.user.email, 'password': 'qwerty'})

        self.access_token = response.data.get('access')  # Токен для авторизации

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)  # Авторизация пользователя

        # Создаем приятную привычку
        self.pleasant_habit = Habit.objects.create(place='дом',
                                                   habit_time='21:00',
                                                   action='Видеоигра',
                                                   is_pleasant=True,
                                                   periodicity=1,
                                                   execution_time='120',
                                                   user=self.user,
                                                   is_public=True
                                                   )

        # Создаем привычку
        self.habit = Habit.objects.create(place='спортплощадка',
                                          habit_time='07:00',
                                          action='Зарядка',
                                          is_pleasant=False,
                                          periodicity=1,
                                          related_habit=self.pleasant_habit,
                                          execution_time='120',
                                          user=self.user
                                          )

    def test_create_habit(self):
        """Тестируем создание привычки"""

        # данные для привычки
        data = {
            'place': 'дом',
            'habit_time': '20:00',
            'action': 'чтение',
            'is_pleasant': False,
            'periodicity': 1,
            'award': 'сладость',
            'execution_time': '100',
            'user': self.user
        }

        response = self.client.post(reverse('spa:create_habit'), data=data)  # отправка запроса
        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # проверяем статус ответа

        self.assertEqual(Habit.objects.all().count(), 3)  # проверяем наличия в базе данных новой записи

    def test_update_habit(self):
        """тестирование изменения привычки"""
        data = {'place': 'спортплощадка обновленная',
                'habit_time': '07:00',
                'action': 'Зарядка',
                'is_pleasant': False,
                'periodicity': 1,
                'related_habit': self.pleasant_habit.pk,
                'execution_time': '120',
                'user': self.user.pk
                }

        response = self.client.put(reverse('spa:update_habit', args=[self.habit.pk]), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка статуса ответа
        self.assertEqual(self.habit.place, 'спортплощадка обновленная')

    def test_list_habits(self):
        response = self.client.get(reverse('spa:habit_list'))  # Запрос на получение списка привычек

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверка ответа на запрос
    def test_destroy_habit(self):
        response = self.client.delete(reverse('spa:delete', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

        self.assertEqual(Habit.objects.all().count(), 1)  # Проверка количества записей уроков в БД

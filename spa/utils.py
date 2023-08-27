import requests

from config import settings


def send_telegram_message(habit):
    """функция для отправки сообщения в теграмм"""
    token = settings.TELEGRAM_TOKEN  # токен для телеграмм бота
    award = habit.award if habit.award else habit.related_habit.action  # вознаграждение за выполненную привычку

    # текст для отправки в телеграмм
    text = (f'Привет. Это напоминание о привычке:'
            f' место - {habit.place}, действие - {habit.action}, время выполнения - {habit.execution_time},'
            f' вознаграждение - {award}')

    data = {'chat_id': '396295095', 'text': text}  # данные для формирования url

    # отправка сообщения пользователю
    response = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?', data=data)


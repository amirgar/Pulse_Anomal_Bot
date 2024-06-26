import telebot
from ai_pulse_anomaly_detector import ai
from telebot import types
from config import token


token = token
data_user = []


# Создаем экземпляр бота
bot = telebot.TeleBot(token)
# 1 4 26272 363738


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    ready_button = types.KeyboardButton("Готов!")
    keyboard.add(ready_button)
    bot.send_message(m.chat.id, 'Привет! Я бот, который умеет определять патологии сердца. Принцип работы схожий с '
                                'методикой ЭКГ - в обоих методах рассматриваются схожие параметры: возраст, пол, тип '
                                'боли, артериальное давление, максимальная достигнутая частота сердечных сокращений и '
                                'была ли когда-то стенокардия. '
                                'Предупреждаю тебя сразу о двух вещах: во-первых, точность моих вычислений равна ~84%, '
                                'поэтому возможны небольшие неточности, но я стараюсь улучшаться :) \nВо-вторых, если '
                                'у тебя есть такой диагноз, как сахарный диабет, то такой метод исследования твоего '
                                'сердца, к сожалению, не сработает. При возможных вопросах рекомендую обратиться'
                                ' к врачу. '
                                'Если ты готов, нажми на кнопку ниже!', reply_markup=keyboard)

@bot.message_handler(content_types=['helpp'])
def help(m, res=False):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    ready_button = types.KeyboardButton("Готов!")
    keyboard.add(ready_button)
    bot.send_message(m.chat.id, 'В этом разделе вы можете узнать подробную информацию: \n'
                                'Стенокардия - https://yandex.ru/turbo?text=https%3A%2F%2Fhealth.yandex.ru%'
                                '2Fdiseases%2Fvasorum%2Fstenocardia\n'
                                'Типичная стенокардия (тип боли №1) - https://clck.ru/39fPqJ\n'
                                'Атипичная стенокардия (тип боли №2) - https://clck.ru/39fPqd\n'
                                'Не ангинальная стенокардия (тип боли №3) - https://clck.ru/39fPqr\n'
                                'Если ты готов, нажми на кнопку ниже!', reply_markup=keyboard)


# Получение сообщений от пользователя
# 28 1 2 130 185 0
# 46 1 4 120 115 1
@bot.message_handler(content_types=["text"])
def start_work(m, res=False):
    if m.text == 'Готов!':
        bot.send_message(m.chat.id, f'Отлчино! Введи через пробел следующие данные:\n'
                         f'1. Возраст\n'
                         f'2. Пол (женщина/мужчина)\n'
                         f'3. Тип боли: \n'
                         f'Если типичная стенокардия - введите цифру 1\n'
                         f'Если атипичная стенокардия - введите цифру 2\n'
                         f'Если не ангинальная стенокардия - введите цифру 3\n'
                         f'Если ничего не чувствуете - введите цифру 4\n'
                         'Стенокардия - https://yandex.ru/turbo?text=https%3A%2F%2Fhealth.yandex.ru%'
                         '2Fdiseases%2Fvasorum%2Fstenocardia\n'
                         'Типичная стенокардия (тип боли №1) - https://clck.ru/39fPqJ\n'
                         'Атипичная стенокардия (тип боли №2) - https://clck.ru/39fPqd\n'
                         'Не ангинальная стенокардия (тип боли №3) - https://clck.ru/39fPqr\n'
                         f'4. Артериальное давление (в состоянии покоя)\n'
                         f'5. Максимальное достигнутая частота сердечных сокращений\n'
                         f'6. Была ли у вас стенокардия при физических нагрузках? (да/нет)\n'
                         f'Пожалуйста, вводите данные через пробел, иначе мне не удастся вывести вам ответ!\n'
                         f'Например: 28 женщина 2 130 185 да')
    else:
        data = list(m.text.split(' '))

        if int(data[0]) <= 0:
            bot.send_message(m.chat.id, f'Введен неверный возраст. Введите /start для возобновления работы бота')
            return
        if data[1].lower() != 'женщина' and data[1].lower() != 'мужчина':
            bot.send_message(m.chat.id, f'Некорректно введен пол. Введите /start для возобновления работы бота')
            return
        elif data[1].lower() == 'мужчина':
            data[1] = 1
        elif data[1].lower() == 'женщина':
            data[1] = 0
        if data[-1].lower() != 'да' and data[-1].lower() != 'нет':
            bot.send_message(m.chat.id, f'Вы неправильно ввели шестой параметр. Введите /start для возобновления работы бота')
            return
        elif data[-1].lower() == 'да':
            data[-1] = 1
        else:
            data[-1] = 0
        data = list(map(int, data))
        if not (0 < data[2] < 5):
            bot.send_message(m.chat.id,
                             f'Вы неправильно ввели тип боли. Введите /start для возобновления работы бота')
            return
        if not (50 < data[-2] < 250):
            bot.send_message(m.chat.id,
                             f'Слишком большое артериальное давление. Скорее всего у вас патологии сердца. Рекомендуется обратиться к врачу с таким показателем давления. Введите /start для возобновления работы бота')
            return
        if not (33 < data[-2] < 220):
            bot.send_message(m.chat.id,
                             f'Слишком большая частота сердечных сокращений. Скорее всего у вас патологии сердца. Рекомендуется обратиться к врачу с таким показателем ЧСС. Введите /start для возобновления работы бота')
            return
        try:
            bot.send_message(m.chat.id, f'{ai(data)}. Если хотите начать заново, нажмите на кнопку')
        except:
            bot.send_message(m.chat.id,
                             f'Вы неправильно ввели данные. Следуйте указанному примеру. Введите /start для возобновления работы бота')


bot.polling(none_stop=True, interval=0)

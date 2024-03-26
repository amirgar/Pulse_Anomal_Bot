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
                                'Предупреждаю тебя сразу о двух вещах: во-первых, точность моих вычислений равна ~93%, '
                                'поэтому возможны небольшие неточности, но я стараюсь улучшаться :) \nВо-вторых, если '
                                'у тебя есть такой диагноз, как сахарный диабет, то такое метод исследования твоего '
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
                                'Типичная стенокардия (тип боли №1) - https://www.invitro.ru/library/bolezni/27553/#:~:text=%D0%A1%D1%82%D0%B5%D0%BD%D0%BE%D0%BA%D0%B0%D1%80%D0%B4%D0%B8%D1%8F%20%E2%80%93%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%B8%D0%BD%D0%B4%D1%80%D0%BE%D0%BC%2C%20%D0%BF%D1%80%D0%BE%D1%8F%D0%B2%D0%BB%D1%8F%D1%8E%D1%89%D0%B8%D0%B9%D1%81%D1%8F,%D0%BE%D1%82%201%20%D0%B4%D0%BE%2015%20%D0%BC%D0%B8%D0%BD%D1%83%D1%82\n'
                                'Атипичная стенокардия (тип боли №2) - https://meduniver.com/Medical/cardiologia/253.html?ysclid=lu7d4tmph2213335358#:~:text=%D0%90%D1%82%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%B5%20%D0%B2%D0%B8%D0%B4%D1%8B%20%D1%81%D1%82%D0%B5%D0%BD%D0%BE%D0%BA%D0%B0%D1%80%D0%B4%D0%B8%D0%B8%20%D1%85%D0%B0%D1%80%D0%B0%D0%BA%D1%82%D0%B5%D1%80%D0%B8%D0%B7%D1%83%D1%8E%D1%82%D1%81%D1%8F%20%D0%BE%D1%82%D1%81%D1%83%D1%82%D1%81%D1%82%D0%B2%D0%B8%D0%B5%D0%BC%20%D1%82%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B1%D0%BE%D0%BB%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D1%80%D0%B8%D1%81%D1%82%D1%83%D0%BF%D0%B0%20%D0%B8%20%D0%BF%D0%BE%D1%8F%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC%20%D0%BD%D0%B0%20%D1%84%D0%BE%D0%BD%D0%B5%20%D0%B8%D1%88%D0%B5%D0%BC%D0%B8%D0%B8%20%D0%BC%D0%B8%D0%BE%D0%BA%D0%B0%D1%80%D0%B4%D0%B0%20(%D0%BE%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%20%D1%83%20%D0%BF%D0%BE%D0%B6%D0%B8%D0%BB%D1%8B%D1%85%20%D0%B1%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D1%85)%20%D0%B4%D1%80%D1%83%D0%B3%D0%B8%D1%85%2C%20%D0%BC%D0%B5%D0%BD%D0%B5%D0%B5%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D1%87%D0%BD%D1%8B%D1%85%20%D1%81%D0%B8%D0%BC%D0%BF%D1%82%D0%BE%D0%BC%D0%BE%D0%B2%20(%D0%BE%D0%B4%D1%8B%D1%88%D0%BA%D0%B0%2C%20%D0%B0%D1%80%D0%B8%D1%82%D0%BC%D0%B8%D1%8F%2C%20%D1%82%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D1%8C%2C%20%D1%83%D1%81%D1%82%D0%B0%D0%BB%D0%BE%D1%81%D1%82%D1%8C%2C%20%D0%B8%D0%B7%D0%B6%D0%BE%D0%B3%D0%B0%20%D0%B8%20%D0%BF%D1%80.).%20%D0%9F%D1%80%D0%B8%D0%BD%D1%8F%D1%82%D0%BE%20%D0%B2%D1%8B%D0%B4%D0%B5%D0%BB%D1%8F%D1%82%D1%8C%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B8%D0%B5%20%D0%B0%D1%82%D0%B8%D0%BF%D0%B8%D1%87%D0%BD%D1%8B%D0%B5%20%D0%B2%D0%B8%D0%B4%D1%8B%20%D0%A1%D1%82%3A\n'
                                'Неангинальная стенокардия (тип боли №3) - https://meduniver.com/Medical/cardiologia/280.html?ysclid=lu7d8nui1y950280876#:~:text=%D0%BF%D0%BE%D0%B2%D1%8B%D1%88%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F%20%D0%BF%D0%BE%D1%82%D0%BB%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D1%8C%2C%20%D0%BE%D0%B4%D1%8B%D1%88%D0%BA%D0%B0%2C%20%D1%83%D1%81%D1%82%D0%B0%D0%BB%D0%BE%D1%81%D1%82%D1%8C%2C%20%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%BA%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2C%20%D0%BE%D0%B1%D0%BC%D0%BE%D1%80%D0%BE%D0%BA%D0%B8%2C%20%D0%B0%20%D1%82%D0%B0%D0%BA%D0%B6%D0%B5%20%D0%B4%D0%B8%D1%81%D0%BF%D0%B5%D0%BF%D1%81%D0%B8%D1%8F%20%D0%B8%20%D1%80%D0%B2%D0%BE%D1%82%D0%B0n\n'
                                'Если ты готов, нажми на кнопку ниже!', reply_markup=keyboard)


# Получение сообщений от пользователя
# 28 1 2 130 185 0
# 46 1 4 120 115 1
@bot.message_handler(content_types=["text"])
def start_work(m, res=False):
    if m.text == 'Готов!':
        bot.send_message(m.chat.id, f'Отлчино! Введи через пробел следующие данные:'
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
        data = map(int, data)
        try:
            bot.send_message(m.chat.id, f'{ai(data)}. Если хотите начать заново, нажмите на кнопку')
        except:
            bot.send_message(m.chat.id,
                             f'Вы неправильно ввели данные. Следуйте указанному примеру. Введите /start для возобновления работы бота')



bot.polling(none_stop=True, interval=0)


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from services.file_handling import get_random_word
from database.database import users_db


def create_menu_button() -> ReplyKeyboardBuilder:
    # Кнопка показать меню
    # Инициализируем билдер
    menu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    # Создаем список с кнопками
    menu_button = KeyboardButton(text='Показать меню ⭐')
    # Распаковываем список с кнопками в билдер, указываем, что
    # в одном ряду должно быть 4 кнопки
    menu_builder.row(menu_button)
    return menu_builder.as_markup(resize_keyboard=True)

def create_start_menu_buttons() -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    type_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_words: InlineKeyboardButton = InlineKeyboardButton(text='Перейти к обучению 💫',
                                                             callback_data='starting')
    type_builder.row(button_words, width=1)
    return type_builder.as_markup(resize_keyboard=True)

def create_type_buttons() -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    type_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_words: InlineKeyboardButton = InlineKeyboardButton(text='Учить слова 📔',
                                                             callback_data='words')
    button_rules: InlineKeyboardButton = InlineKeyboardButton(text='Учить правила 📝',
                                                             callback_data='rules')
    type_builder.row(button_words, width=1)
    type_builder.row(button_rules, width=1)
    return type_builder.as_markup(resize_keyboard=True)

def create_lists_words_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором слов
    lists_words_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_400_words: InlineKeyboardButton = InlineKeyboardButton(text='Топ 400+ популярных 🥇',
                                                              callback_data='list400')
    button_100_verb: InlineKeyboardButton = InlineKeyboardButton(text='Топ 100 глаголов 🚩',
                                                              callback_data='100verb')
    button_numbers: InlineKeyboardButton = InlineKeyboardButton(text='Цифры и числа 1️⃣2️⃣',
                                                                 callback_data='numbers')
    button_themes: InlineKeyboardButton = InlineKeyboardButton(text='По темам 🏚👨‍👩‍👦🍔',
                                                                callback_data='themes')
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    lists_words_builder.row(button_400_words, width=1)
    lists_words_builder.row(button_numbers, width=1)
    lists_words_builder.row(button_100_verb, width=1)
    lists_words_builder.row(button_themes, width=1)
    lists_words_builder.row(back_button, width=1)
    return lists_words_builder.as_markup(resize_keyboard=True)

def create_lists_rules_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором правил
    lists_words_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_ser: InlineKeyboardButton = InlineKeyboardButton(text='Глагол SER 🕺',
                                                              callback_data='ser')
    button_estar: InlineKeyboardButton = InlineKeyboardButton(text='Глагол ESTAR 💃',
                                                              callback_data='estar')
    button_ser_p: InlineKeyboardButton = InlineKeyboardButton(text='Глагол SER с прилагательными 🧑‍🏫',
                                                                 callback_data='ser_pr')
    button_estar_p: InlineKeyboardButton = InlineKeyboardButton(text='Глагол ESTAR с прилагательными 😜',
                                                                callback_data='estar_pr')
    button_r_verbs: InlineKeyboardButton = InlineKeyboardButton(text='Правильные глаголы 👌',
                                                                callback_data='r_verb')
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    lists_words_builder.row(button_ser, width=1)
    lists_words_builder.row(button_estar, width=1)
    lists_words_builder.row(button_ser_p, width=1)
    lists_words_builder.row(button_estar_p, width=1)
    lists_words_builder.row(button_r_verbs, width=1)
    lists_words_builder.row(back_button, width=1)
    return lists_words_builder.as_markup(resize_keyboard=True)

def create_lists_themes_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    lists_words_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_colors: InlineKeyboardButton = InlineKeyboardButton(text='Цвета 🌈',
                                                              callback_data='colors')
    button_family: InlineKeyboardButton = InlineKeyboardButton(text='Семья 👨‍👩‍👦',
                                                              callback_data='family')
    button_emotions: InlineKeyboardButton = InlineKeyboardButton(text='Эмоции 🤪',
                                                                 callback_data='emotions')
    button_body: InlineKeyboardButton = InlineKeyboardButton(text='Тело 💪',
                                                                callback_data='body')
    button_face: InlineKeyboardButton = InlineKeyboardButton(text='Лицо 👄',
                                                             callback_data='face')
    button_health: InlineKeyboardButton = InlineKeyboardButton(text='Здоровье 💊',
                                                             callback_data='health')
    button_education: InlineKeyboardButton = InlineKeyboardButton(text='Учеба 📚',
                                                               callback_data='education')
    button_weather: InlineKeyboardButton = InlineKeyboardButton(text='Погода 🌤',
                                                                  callback_data='weather')

    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    lists_words_builder.row(button_colors, button_family, button_emotions, button_body, button_face,
                            button_health, button_education, button_weather,
                            width=2)
    lists_words_builder.row(back_button, width=1)
    return lists_words_builder.as_markup(resize_keyboard=True)

def create_days_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    days_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    days_builder.row(*[InlineKeyboardButton(text=f'Занятие {i}', callback_data=f'day_{i}') for i in range(1,6)], width=1)
    days_builder.row(back_button, width=1)
    return days_builder.as_markup(resize_keyboard=True)

def create_400_task_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    tasks_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_esrus : InlineKeyboardButton = InlineKeyboardButton(text='Переведи слово Español-Русский 🇦🇷🇷🇺',
                                                               callback_data='esp1')
    button_ruses: InlineKeyboardButton = InlineKeyboardButton(text='Переведи слово Русский-Español 🇷🇺🇦🇷',
                                                              callback_data='rus1')
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    tasks_builder.row(button_esrus, width=1)
    tasks_builder.row(button_ruses, width=1)
    tasks_builder.row(back_button, width=1)
    return tasks_builder.as_markup(resize_keyboard=True)

def create_verb_rules_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    tasks_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_esrus: InlineKeyboardButton = InlineKeyboardButton(text='Выбери верную форму глагола 🇦🇷',
                                                               callback_data='verbs_t')
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    tasks_builder.row(button_esrus, width=1)
    tasks_builder.row(back_button, width=1)
    return tasks_builder.as_markup(resize_keyboard=True)

def create_r_verb_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    tasks_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_esrus: InlineKeyboardButton = InlineKeyboardButton(text='Выбери верное склонение глагола 🇦🇷',
                                                               callback_data='verbs_sk')
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    tasks_builder.row(button_esrus, width=1)
    tasks_builder.row(back_button, width=1)
    return tasks_builder.as_markup(resize_keyboard=True)


def create_task_buttons(page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором курсов
    tasks_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_dict: InlineKeyboardButton = InlineKeyboardButton(text='Показать список слов 📃',
                                                              callback_data='dict1')
    button_esrus : InlineKeyboardButton = InlineKeyboardButton(text='Переведи слово Español-Русский 🇦🇷🇷🇺',
                                                               callback_data='esp1')
    button_ruses: InlineKeyboardButton = InlineKeyboardButton(text='Переведи слово Русский-Español 🇷🇺🇦🇷',
                                                              callback_data='rus1')
    button_estask: InlineKeyboardButton = InlineKeyboardButton(text='Выбери форму глагола 🇦🇷',
                                                              callback_data='task_3')
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    tasks_builder.row(button_dict, width=1)
    tasks_builder.row(button_esrus, width=1)
    tasks_builder.row(button_ruses, width=1)
    tasks_builder.row(button_estask, width=1)
    tasks_builder.row(back_button, width=1)
    return tasks_builder.as_markup(resize_keyboard=True)

def create_answer_buttons(callback: CallbackQuery, ruwords, page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором ответа
    word = ruwords[users_db[callback.from_user.id]['word']]
    days_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    l = get_random_word(word, ruwords)
    days_builder.row(*[InlineKeyboardButton(text=f'{key}', callback_data=f'{value}') for key, value in l.items()], width=1)
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    days_builder.row(back_button, width=1)
    return days_builder.as_markup(resize_keyboard=True)

def create_num_answer_buttons(callback: CallbackQuery, numwords, page) -> InlineKeyboardMarkup:
    # создаю клавиатуру с выбором ответа
    word = numwords[users_db[callback.from_user.id]['word']]
    days_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    l = get_random_num(word, numwords)
    days_builder.row(*[InlineKeyboardButton(text=f'{key}', callback_data=f'{value}') for key, value in l.items()], width=1)
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    days_builder.row(back_button, width=1)
    return days_builder.as_markup(resize_keyboard=True)

def create_back_button(page) -> InlineKeyboardMarkup:
    # создаю кнопку назад
    days_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    back_button: InlineKeyboardButton = InlineKeyboardButton(text='Назад ⬅️', callback_data=f'{page}')
    days_builder.row(back_button, width=1)
    return days_builder.as_markup(resize_keyboard=True)






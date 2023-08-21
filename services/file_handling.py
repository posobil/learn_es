import os
import random
from lexicon.words import WORDS_ES_RUS, Day_1_task_2
import gspread

dict_esrus = WORDS_ES_RUS
eswords: list = []
ruwords: list = []
table_link = 'https://docs.google.com/spreadsheets/d/1ql3rtO1UCK0TIwL0NOskyjnRzb2lMjKwHWuLo9DuLW8/edit?usp=sharing'


# Метод принимает ссылку на гугл таблицу и название страницы
# возвращает 2 списка из первого и второго столбцов выбранной страницы
def check_user_in_table(table_link, user_name):
    gc = gspread.service_account(filename='qta.json')
    sh = gc.open_by_url(table_link)
    worksheet = sh.worksheet('users')
    users = worksheet.col_values(1)
    if user_name in users:
        return True
    else:
        return False

# Метод принимает ссылку на гугл таблицу и название страницы
# Записывает в новую ячейку первого столбца ник пользователя
def add_user_in_table(table_link, user_name):
    gc = gspread.service_account(filename='qta.json')
    sh = gc.open_by_url(table_link)
    worksheet = sh.worksheet('users')
    users = worksheet.col_values(1)
    num_cell = len(users) + 1
    worksheet.update_cell(num_cell, 1, user_name)
    pass

# Метод принимает ссылку на гугл таблицу и название страницы
# возвращает 2 списка из первого и второго столбцов выбранной страницы
def get_words_lists_gtable(table_link, page_name):
    gc = gspread.service_account(filename='qta.json')
    sh = gc.open_by_url(table_link)
    worksheet = sh.worksheet(page_name)
    es_w = worksheet.col_values(1)
    ru_w = worksheet.col_values(2)
    return es_w, ru_w

# Метод принимает ссылку на гугл таблицу и название страницы
# возвращает 2 списка из первого и второго столбцов выбранной страницы (20 рандомных слов)
def get_words_lists_gtable_randome(table_link, page_name, number):
    num = number
    gc = gspread.service_account(filename='qta.json')
    sh = gc.open_by_url(table_link)
    worksheet = sh.worksheet(page_name)
    es_w = worksheet.col_values(1)
    ru_w = worksheet.col_values(2)
    f_es = []
    f_ru = []
    i = 0
    while i < num:
        s = random.randint(0, len(es_w) - 1)
        if es_w[s] not in f_es:
            f_es.append(es_w[s])
            f_ru.append(ru_w[s])
            i += 1
    return f_es, f_ru


# Преобразую в строку для вывода всего набора слов
def listdict_es_rus(es_list, ru_list):
    ll = ''
    for i in range(len(es_list)):
        ll = ll + (f'{es_list[i]} - {ru_list[i]}\n')
    return ll

# функция принимае массив и возвращает 2 списка слов
def get_es_rus_lists(dict):
    es_words: list = []
    ru_words: list = []
    for key, value in dict.items():
        es_words.append(key)
        ru_words.append(value)
    return es_words, ru_words

def get_ru_es(ru_list, es_list):
    dict_ru_es = {}
    for i in range(len(ru_list)):
        dict_ru_es[ru_list[i]] = es_list[i]
    return dict_ru_es


# функция принимает выбранное корректное слово и список слов
# возвращает словарь с корректным словом и 3я рандомными(с сортировкой)
def get_random_word(correct_word, words):
    words_dict: dict[str, str] = {}
    words_dict[correct_word] = 'correct'
    while True:
        number = random.randint(0, len(words) - 1)
        if correct_word != words[number]:
            words_dict[words[number]] = 'incorrect'
            if len(words_dict) == 4:
                break
    sort_words = sorted(words_dict.items())
    return dict(sort_words)


def get_random_word_ru(correct_word, words):
    words_dict: dict[str, str] = {}
    words_dict[correct_word] = 'correct'
    while True:
        number = random.randint(0, len(words) - 1)
        if correct_word != words[number]:
            words_dict[words[number]] = 'incorrect'
            if len(words_dict) == 4:
                break
    sort_words = sorted(words_dict.items())
    return dict(sort_words)

def get_random_task_3(correct_word, words):
    words_dict: dict[str, str] = {}
    words_dict[correct_word] = 'right'
    while True:
        number = random.randint(0, len(words) - 1)
        if correct_word != words[number]:
            words_dict[words[number]] = 'wrong'
            if len(words_dict) == 4:
                break
    sort_words = sorted(words_dict.items())
    return dict(sort_words)

eswords, ruwords = get_es_rus_lists(WORDS_ES_RUS)
estask2, esansw2 = get_es_rus_lists(Day_1_task_2)

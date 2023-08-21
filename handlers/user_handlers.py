import random
from copy import deepcopy
from aiogram import Router, F
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from keyboards.pagination_kb import create_menu_button, create_type_buttons,\
    create_lists_words_buttons, create_400_task_buttons, create_answer_buttons, create_back_button, \
    create_lists_themes_buttons, create_lists_rules_buttons, create_verb_rules_buttons, \
    create_start_menu_buttons, create_r_verb_buttons
from lexicon.lexicon import LEXICON
from services.file_handling import get_words_lists_gtable_randome, table_link, check_user_in_table, add_user_in_table
from database.database import user_dict_template, users_db

router: Router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message):
    if check_user_in_table(table_link, message.from_user.username):
        await message.answer(LEXICON['/start'], reply_markup=create_menu_button())
    else:
        add_user_in_table(table_link, message.from_user.username)
        await message.answer(LEXICON['/start'], reply_markup=create_menu_button())

@router.message(F.text=='Показать меню ⭐')
async def open_menu(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = deepcopy(user_dict_template)
    users_db[message.from_user.id]['correct'] = 0
    await message.answer(LEXICON['starting'], reply_markup=create_start_menu_buttons())

@router.callback_query(Text(text='starting'))
async def st_learn(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'starting'
    await callback.message.edit_text(
            text=LEXICON['starting'],
            reply_markup=create_type_buttons())

"""Выбор слов или правил"""
@router.callback_query(Text(text='words'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'starting'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=LEXICON['choise_list'],
            reply_markup=create_lists_words_buttons(page))

@router.callback_query(Text(text='rules'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'starting'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=LEXICON['choise_rules'],
            reply_markup=create_lists_rules_buttons(page))


"""Хэнедлеры правил"""
@router.callback_query(Text(text='ser'))
async def process_verbs(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'rules'
    users_db[callback.from_user.id]['w_list'] = 'ser'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=f'{LEXICON["/ser1"]}'
                 '<a href="https://telegra.ph/Glagol-SER-08-20"><u>Глагол SER</u></a>\n\n'
                 f'{LEXICON["/verb_fin"]}', disable_web_page_preview=True,
            reply_markup=create_verb_rules_buttons(page))

@router.callback_query(Text(text='estar'))
async def process_verbs1(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'rules'
    users_db[callback.from_user.id]['w_list'] = 'estar'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
        text=f'{LEXICON["/estar1"]}'
             '<a href="https://telegra.ph/Glagol-ESTAR-08-20"><u>Глагол ESTAR</u></a>\n\n'
             f'{LEXICON["/verb_fin"]}', disable_web_page_preview=True,
        reply_markup=create_verb_rules_buttons(page))

@router.callback_query(Text(text='ser_pr'))
async def process_verbs(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'rules'
    users_db[callback.from_user.id]['w_list'] = 'ser_pr'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=f'{LEXICON["/ser1"]} '
                 '<a href="https://telegra.ph/Glagol-SER-s-prilagatelnymi-08-20"><u>Глагол SER с прилагательными</u></a>\n\n'
                 f'{LEXICON["/verb_fin"]}', disable_web_page_preview=True,
            reply_markup=create_verb_rules_buttons(page))

@router.callback_query(Text(text='estar_pr'))
async def process_verbs(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'rules'
    users_db[callback.from_user.id]['w_list'] = 'estar_pr'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=f'{LEXICON["/ser1"]} '
                 '<a href="https://telegra.ph/Glagol-ESTAR-s-prilagatelnymi-08-20"><u>Глагол ESTAR с прилагательными</u></a>\n\n'
                 f'{LEXICON["/verb_fin"]}', disable_web_page_preview=True,
            reply_markup=create_verb_rules_buttons(page))

@router.callback_query(Text(text='r_verb'))
async def process_r_verbs(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'rules'
    users_db[callback.from_user.id]['w_list'] = 'r_verb'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=f'{LEXICON["r_verb"]}'
                 '<a href="https://telegra.ph/Sklonenie-pravilnyh-glagolov-08-21"><u>Склонение глаголов (правильных)</u></a>\n\n'
                 '<a href="https://telegra.ph/Top-20-pravilnyh-glagolov-08-21"><u>Топ-20 правильных глаголов</u></a>\n\n'
                 f'{LEXICON["/verb_fin"]}', disable_web_page_preview=True,
            reply_markup=create_r_verb_buttons(page))


"""Хэнедлеры слов"""
@router.callback_query(Text(text='list400'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'words'
    users_db[callback.from_user.id]['w_list'] = 'list400'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=LEXICON["choise_type_task"],
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='100verb'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'words'
    users_db[callback.from_user.id]['w_list'] = '100verb'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Top-100-glagolov-08-20">👉Посмотреть список слов👈</a>'
             f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='numbers'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'words'
    users_db[callback.from_user.id]['w_list'] = 'numbers'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Cifry-i-chisla-08-20">👉Посмотреть список слов👈</a>'
             f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='themes'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'words'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text=LEXICON["choise_theme"],
            reply_markup=create_lists_themes_buttons(page))

@router.callback_query(Text(text='colors'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'colors'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Cveta-08-20">👉Посмотреть список слов👈</a>'
             f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='family'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'family'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Semya-08-20-2">👉Посмотреть список слов👈</a>'
             f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='emotions'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'emotions'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/EHmocii-08-20">👉Посмотреть список слов👈</a>'
             f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='body'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'body'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Telo-08-19">👉Посмотреть список слов👈</a>'
             f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='face'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'face'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Cveta-08-19-2">👉Посмотреть список слов👈</a>'
                 f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='health'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'health'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Zdorove-08-20">👉Посмотреть список слов👈</a>'
                 f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='education'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'education'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Ucheba-08-20">👉Посмотреть список слов👈</a>'
                 f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))

@router.callback_query(Text(text='weather'))
async def process_forward_press(callback: CallbackQuery):
    users_db[callback.from_user.id]['page'] = 'themes'
    users_db[callback.from_user.id]['w_list'] = 'weather'
    page = users_db[callback.from_user.id]['page']
    await callback.message.edit_text(
            text='<a href="https://telegra.ph/Pogoda-08-20">👉Посмотреть список слов👈</a>'
                 f'\n{LEXICON["choise_type_task"]}', disable_web_page_preview=True,
            reply_markup=create_400_task_buttons(page))


"""Хэнедлеры для ответов и запуска заданий (верно/не верно)"""
@router.callback_query(Text(text='esp1'))
async def start_translate_es_ru(callback: CallbackQuery):
    choose_task = users_db[callback.from_user.id]['w_list']
    users_db[callback.from_user.id]['page'] = choose_task
    es, ru = get_words_lists_gtable_randome(table_link, choose_task, 10)
    users_db[callback.from_user.id]['list_1'] = es
    users_db[callback.from_user.id]['list_2'] = ru
    list_1 = users_db[callback.from_user.id]['list_1']
    list_2 = users_db[callback.from_user.id]['list_2']
    users_db[callback.from_user.id]['correct'] = 0
    users_db[callback.from_user.id]['word'] = 0
    word = list_1[users_db[callback.from_user.id]['word']]
    await callback.message.edit_text(
        text=f'{users_db[callback.from_user.id]["word"] + 1}/{len(list_1)}\n'
             f'{LEXICON["/trans"]}<b>{word}</b>', reply_markup=create_answer_buttons(callback, list_2, choose_task))

@router.callback_query(Text(text='rus1'))
async def start_translate_ru_es(callback: CallbackQuery):
    choose_task = users_db[callback.from_user.id]['w_list']
    users_db[callback.from_user.id]['page'] = choose_task
    es, ru = get_words_lists_gtable_randome(table_link, choose_task, 10)
    users_db[callback.from_user.id]['list_1'] = ru
    users_db[callback.from_user.id]['list_2'] = es
    list_1 = users_db[callback.from_user.id]['list_1']
    list_2 = users_db[callback.from_user.id]['list_2']
    users_db[callback.from_user.id]['correct'] = 0
    users_db[callback.from_user.id]['word'] = 0
    word = list_1[users_db[callback.from_user.id]['word']]
    await callback.message.edit_text(
        text=f'{users_db[callback.from_user.id]["word"] + 1}/{len(list_1)}\n'
             f'{LEXICON["/trans"]}<b>{word}</b>', reply_markup=create_answer_buttons(callback, list_2, choose_task))

@router.callback_query(Text(text='verbs_t'))
async def start_verbs_t(callback: CallbackQuery):
    choose_task = users_db[callback.from_user.id]['w_list']
    users_db[callback.from_user.id]['page'] = choose_task
    es, ru = get_words_lists_gtable_randome(table_link, choose_task, 10)
    users_db[callback.from_user.id]['list_1'] = es
    users_db[callback.from_user.id]['list_2'] = ru
    list_1 = users_db[callback.from_user.id]['list_1']
    list_2 = users_db[callback.from_user.id]['list_2']
    users_db[callback.from_user.id]['correct'] = 0
    users_db[callback.from_user.id]['word'] = 0
    word = list_1[users_db[callback.from_user.id]['word']]
    await callback.message.edit_text(
        text=f'{users_db[callback.from_user.id]["word"] + 1}/{len(list_1)}\n'
             f'{LEXICON["/verb"]}<b>{word}</b>', reply_markup=create_answer_buttons(callback, list_2, choose_task))

@router.callback_query(Text(text='verbs_sk'))
async def start_verbs_t(callback: CallbackQuery):
    choose_task = users_db[callback.from_user.id]['w_list']
    users_db[callback.from_user.id]['page'] = choose_task
    es, ru = get_words_lists_gtable_randome(table_link, choose_task, 10)
    users_db[callback.from_user.id]['list_1'] = es
    users_db[callback.from_user.id]['list_2'] = ru
    list_1 = users_db[callback.from_user.id]['list_1']
    list_2 = users_db[callback.from_user.id]['list_2']
    users_db[callback.from_user.id]['correct'] = 0
    users_db[callback.from_user.id]['word'] = 0
    word = list_1[users_db[callback.from_user.id]['word']]
    await callback.message.edit_text(
        text=f'{users_db[callback.from_user.id]["word"] + 1}/{len(list_1)}\n'
             f'{LEXICON["/verb_sk"]}<b>{word}</b>', reply_markup=create_answer_buttons(callback, list_2, choose_task))

@router.callback_query(Text(text='correct'))
async def translate_es_ru(callback: CallbackQuery):
    page = users_db[callback.from_user.id]['page']
    choose_task = users_db[callback.from_user.id]['w_list']
    list_1 = users_db[callback.from_user.id]['list_1']
    list_2 = users_db[callback.from_user.id]['list_2']
    if users_db[callback.from_user.id]['word'] + 1 < len(list_1):
        users_db[callback.from_user.id]['word'] += 1
        users_db[callback.from_user.id]['correct'] += 1
        word = list_1[users_db[callback.from_user.id]['word']]
        await callback.message.edit_text(
            text=f'{users_db[callback.from_user.id]["word"] + 1}/{len(list_1)}\n'
                    f'{LEXICON["/trans_sh"]}\n<b>{word}</b>', reply_markup=create_answer_buttons(callback, list_2, choose_task))
        await callback.answer(text='✅ Верно')
    else:
        users_db[callback.from_user.id]['word'] += 1
        users_db[callback.from_user.id]['correct'] += 1
        await callback.message.edit_text(
            text=f'{LEXICON["finish"]}{users_db[callback.from_user.id]["correct"] } из {len(list_2)}\n',
            reply_markup=create_back_button(page))
        await callback.answer(text='✅ Верно')


@router.callback_query(Text(text='incorrect'))
async def translate_es_ru_inc(callback: CallbackQuery):
    choose_task = users_db[callback.from_user.id]['w_list']
    page = users_db[callback.from_user.id]['page']
    list_1 = users_db[callback.from_user.id]['list_1']
    list_2 = users_db[callback.from_user.id]['list_2']
    if users_db[callback.from_user.id]['word'] + 1 < len(list_1):
        users_db[callback.from_user.id]['word'] += 1
        word = list_1[users_db[callback.from_user.id]['word']]
        await callback.message.edit_text(
            text=f'{users_db[callback.from_user.id]["word"] + 1}/{len(list_1)}\n'
                    f'{LEXICON["/trans_sh"]}\n<b>{word}</b>', reply_markup=create_answer_buttons(callback, list_2, choose_task))
        await callback.answer(text='❌ Не верно')
    else:
        users_db[callback.from_user.id]['word'] += 1
        await callback.message.edit_text(
            text=f'{LEXICON["finish"]}{users_db[callback.from_user.id]["correct"] } из {len(list_2)}\n',
            reply_markup=create_back_button(page))
        await callback.answer(text='❌ Не верно')

# Этот хэндлер будет срабатывать на команду "/help"
# и отправлять пользователю сообщение со списком доступных команд в боте
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON['/help'])


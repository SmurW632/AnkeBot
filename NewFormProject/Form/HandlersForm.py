#Форма заполнения анкеты пользователем без GPT
from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from Keyboards.InlineKeyboard import *
from Classes.BotClasses import *
import Translate.FuncTranslate as TF
from GPTReauests.RequestsGPT import prompt


router_form = Router()

user_data = {
    "name": "",
    "start": "",
    "end": "",
    "epitaph": "",
    "author_epitaph": "", 
    "page_type_id": "1"
}
'''
Дальше идут обработчики которые направляются по событиям
'''
@router_form.message(StepsBots.FORM)
async def SetName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["name"] = message.text
    await bot.send_message(message.from_user.id, f"{await TF.Translation("Укажите дату рождения", lang)}")
    await state.set_state(StepsFormsTest.GET_DATA_B)

@router_form.message(StepsFormsTest.GET_DATA_B)
async def SetName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["start"] = message.text
    await bot.send_message(message.from_user.id, f"{await TF.Translation("Укажите дату смерти", lang)}")
    await state.set_state(StepsFormsTest.GET_DATA_D)

@router_form.message(StepsFormsTest.GET_DATA_D)
async def SetName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["end"] = message.text
    await bot.send_message(message.from_user.id, f"{await TF.Translation("Напишите краткую информацию о человеке.\nНапример Место рождение, место смерти, супруги, дети, достижения, деятельность и т.п\nЧем больше информации тем лучше будет ответ от Yandex GPT.", lang)}")
    await state.set_state(StepsFormsTest.GET_AI_EPITAPHIA)

@router_form.message(StepsFormsTest.GET_AI_EPITAPHIA)
async def SetName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["epitaph"] = await prompt(message.text, user_data["name"], user_data["start"], user_data["end"])
    if lang == 'ru':
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_ru)
    else:
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_en)
        

'''
Редактирование полей
'''
@router_form.message(StepsEdit.EDIT_FIO)
async def EditName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["name"] = message.text
    if lang == 'ru':
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_ru)
    else:
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_en)
        
@router_form.message(StepsEdit.EDIT_DATE_B)
async def EditName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["start"] = message.text
    if lang == 'ru':
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_ru)
    else:
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_en)
        
@router_form.message(StepsEdit.EPITAPH)
async def EditName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["end"] = message.text
    if lang == 'ru':
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_ru)
    else:
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_en)
        
@router_form.message(StepsEdit.BIOGRAPH)
async def EditName(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    user_data["epitaph"] = await prompt(message.text, user_data["name"], user_data["start"], user_data["end"])
    if lang == 'ru':
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_ru)
    else:
        await bot.send_message(message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_en)

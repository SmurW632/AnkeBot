#Здесь будут храниться колл бэки клавиатуры для формы заполнения анкеты без GPT
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import Translate.FuncTranslate as TF
from Classes.BotClasses import StepsForms
from Form.HandlersForm import user_data
from Keyboards.InlineKeyboard import *
from GPTReauests.RequestsGPT import prompt
from Data.SaveJsonUserData import save_user_data

router_callback = Router()

'''
обработка ФИО пункта сообщений
'''
@router_callback.callback_query(F.data == 'EDIT_FIO')
async def EditName(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', "en")
    user_data["name"] = callback.message.text
    await callback.answer()
    await callback.message.edit_text(f'{await TF.Translation("ВВедите ФИО заново", lang)}')
    user_data["epitaph"] = await prompt(callback.message.text, user_data["name"], user_data["start"], user_data["end"])
    if lang == 'ru':
        await callback.message.edit_text(callback.message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_ru)
    else:
        await callback.message.edit_text(callback.message.from_user.id, f"""
{await TF.Translation("ФИО", lang)} - {user_data["name"]}
{await TF.Translation("Дата рождения", lang)} - {user_data["start"]}
{await TF.Translation("Дата смерти", lang)} - {user_data["end"]}
{await TF.Translation("Эпитафия ", lang)} - {user_data["epitaph"]}
Хотите отредактировать данные или хотите закончить заполнение страницы нажните на одну из кнопок.
""", reply_markup = edit_inf_en)

'''
обработка ДАТЫ ПУНКТА СООБЩЕНИЙ
'''
@router_callback.callback_query(F.data == 'OK_SHORT_INF')
async def CallBackOkShortInf(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', "en")
    try:
        answer_user = callback.message.text.split(',')
        '''user_data["start"] = callback.message.text.split(',')[0]
        user_data["end"] = callback.message.text.split(',')[1]'''
        await callback.answer()
        await callback.message.edit_text(f"{await TF.Translation("Напишите запрос для составления эпитафии", lang)}")
        await state.set_state(StepsForms.GET_AI_EPITAPHIA)
    except:
        await callback.message.answer("Что то пошло не так")
    

@router_callback.callback_query(F.data == "NOT_OK_SHORT_INF")
async def CallBackNotOkShortInf(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', "en")
    await state.set_state(StepsForms.GET_SHORT_INF)
    await callback.answer()
    await callback.message.edit_text(f"{await TF.Translation("Укажите дату рождения, дату смерти. Запишите через запятую", lang)}")

'''
обработка ЭПИТАФИЯ ПУНКТА СООБЩЕНИЙ
'''
@router_callback.callback_query(F.data == 'OK_AI_IPITAPHIA')
async def CallBackOkAiEpitaphia(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', "en")
    answer_GPT = await prompt(callback.message.text + f"{await TF.Translation('Напиши эпитафию для страницы памяти о человеке на основе этого текста. Так же в отдельном предложении укажи автора эпитафии.', lang)}")
    '''user_data["epitaph"] = answer_user[:-1] # здесь будет записыватся ответ из gpt
    user_data["author_epitaph"] = callback.message.text.split('.')[-1]'''
    await callback.answer(f"{await TF.Translation('завершение заполнения', lang)}")
    await callback.message.edit_text(f'{await TF.Translation("Вот эпитафия по вашему запросу: ", lang)}\n{answer_GPT}')
    await state.set_state(StepsForms.FINISH)

@router_callback.callback_query(F.data == "NOT_OK_AI_IPITAPHIA")
async def CallBackNotOkAiEpitaphia(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', "en")
    await state.set_state(StepsForms.GET_AI_EPITAPHIA)
    await callback.answer()
    await callback.message.edit_text(f"{await TF.Translation("Напишите какую эпитафию вы хотите или автора эпитафии", lang)}")

'''
обработка событий для состояние ФИНИШ
'''
@router_callback.callback_query(F.data == 'OK_FINISH')
async def CallBackOkPlace(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Спасибо что воспользовались мной от AnkeBot") #Здесь должна быть функция которая отправляет пользователю ссылку на страницу памяти
    await callback.message.answer("Вот ваша ссылка на страницу памяти")

@router_callback.callback_query(F.data == "NOT_OK_FINISH")
async def CallBackNotOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_BASE_INF)
    await callback.answer("Заполняем данные заново")
    await callback.message.edit_text("Укажите ФИО")

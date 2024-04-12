#Здесь будут храниться колл бэки клавиатуры для формы заполнения анкеты без GPT
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from Forms.ViewForm.ViewFormNoGPT import StepsForms, user_data
from Forms.ViewForm.Keyboards.InlineKEyboards import *
from Forms.Save_user_data_in_json import save_user_data

router_callback = Router()

'''
обработка ФИО пункта сообщений
'''
@router_callback.callback_query(F.data == 'OK_BASE_INF')
async def CallBackOkBaseInf(callback: CallbackQuery, state: FSMContext):
    user_data["name"] = callback.message.text
    #await state.update_data(FIO = callback.message.text)
    await callback.answer('Продолжаем заполнение')
    await callback.message.answer('Укажите дату рождения, дату смерти. Запишите через запятую')
    await state.set_state(StepsForms.GET_SHORT_INF)

@router_callback.callback_query(F.data == "NOT_OK_BASE_INF")
async def CallBackNotOkBaseInf(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_BASE_INF)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text("Укажите ФИО")

'''
обработка ДАТЫ ПУНКТА СООБЩЕНИЙ
'''
@router_callback.callback_query(F.data == 'OK_SHORT_INF')
async def CallBackOkShortInf(callback: CallbackQuery, state: FSMContext):
    answer_user = callback.message.text.split(',')
    user_data["start"] = answer_user[0]
    user_data["end"] = answer_user[1]
    #await state.update_data(PHOTO = callback.message.photo)
    await callback.answer()
    await callback.message.answer("Напишите краткую эпитафию и отдельным предложением укажите автора")
    await state.set_state(StepsForms.GET_AI_EPITAPHIA)

@router_callback.callback_query(F.data == "NOT_OK_SHORT_INF")
async def CallBackNotOkShortInf(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_SHORT_INF)
    await callback.answer()
    await callback.message.edit_text("Укажите место рождения, место смерти, дети, супруга/супруг. Все пункты записать через запятую")

'''
обработка ЭПИТАФИЯ ПУНКТА СООБЩЕНИЙ
'''
@router_callback.callback_query(F.data == 'OK_AI_IPITAPHIA')
async def CallBackOkAiEpitaphia(callback: CallbackQuery, state: FSMContext):
    answer_user = callback.message.text.split('.')
    user_data["epitaph"] = answer_user[:-1] # здесь будет записыватся ответ из gpt
    user_data["author_epitaph"] = callback.message.text.split('.')[-1]
    #await state.update_data(PHOTO = callback.message.photo)
    await callback.answer('завершение заполнения')
    await callback.message.answer(f"Вот данные которые вы ввели: ФИО: {user_data["name"]}\nДата рождения: {user_data['start']}\nДата смерти: {user_data["end"]}\nЭпитафия: {user_data["epitaph"]}\nАвтор эпитафии: {user_data["author_epitaph"]}\n Хотите завершенить работу", reply_markup = chek_finish)
    await state.set_state(StepsForms.FINISH)

@router_callback.callback_query(F.data == "NOT_OK_AI_IPITAPHIA")
async def CallBackNotOkAiEpitaphia(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_AI_EPITAPHIA)
    await callback.answer()
    await callback.message.edit_text("Напишите какую эпитафию вы хотите или автора эпитафии")

'''
обработка событий для состояние ФИНИШ
'''
@router_callback.callback_query(F.data == 'OK_FINISH')
async def CallBackOkPlace(callback: CallbackQuery, state: FSMContext):
    await save_user_data(user_data)
    await callback.answer("Спасибо что воспользовались мной от AnkeBot") #Здесь должна быть функция которая отправляет пользователю ссылку на страницу памяти
    await callback.message.answer("Вот ваша ссылка на страницу памяти")

@router_callback.callback_query(F.data == "NOT_OK_FINISH")
async def CallBackNotOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_BASE_INF)
    await callback.answer("Заполняем данные заново")
    await callback.message.edit_text("Укажите ФИО")

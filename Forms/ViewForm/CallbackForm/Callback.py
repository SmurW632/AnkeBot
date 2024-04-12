#Здесь будут храниться колл бэки клавиатуры для формы заполнения анкеты без GPT
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from Forms.ViewForm.ViewFormNoGPT import StepsForms
from Forms.ViewForm.Keyboards.InlineKEyboards import *

router_callback = Router()

'''
обработка коллбэков для пункта ФИО
'''
@router_callback.callback_query(F.data == 'OK_NAME')
async def CallBackOkName(callback: CallbackQuery, state: FSMContext):
    await state.update_data(FIO = callback.message.text)
    await callback.answer('Продолжаем заполнение')
    await callback.message.answer("Пришлите фото для страницы памяти")
    await state.set_state(StepsForms.GET_PHOTO)

@router_callback.callback_query(F.data == "NOT_OK_NAME")
async def CallBackNotOkName(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_NAME_FOR_ANKET)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text("Укажите ФИО")

'''
обработка коллбэков для пункта ФОТО
'''
@router_callback.callback_query(F.data == 'OK_PHOTO')
async def CallBackOkName(callback: CallbackQuery, state: FSMContext):
    await state.update_data(PHOTO = callback.message.photo)
    await callback.answer('Продолжаем заполнение')
    await callback.message.answer("Укажите дату по форме: дд.мм.гг - дд.мм.гг (Между датами тире через пробел)")
    await state.set_state(StepsForms.GET_DATE)

@router_callback.callback_query(F.data == "NOT_OK_PHOTO")
async def CallBackNotOkName(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_PHOTO)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text("Пришлите фото для страницы памяти")

'''
обработка коллбэков для пункта ДАТА
'''
@router_callback.callback_query(F.data == 'OK_DATE')
async def CallBackOkDate(callback: CallbackQuery, state: FSMContext):
    await state.update_data(DATE = callback.message.text)
    await callback.answer('Продолжаем заполнение')
    await callback.message.answer('Укажите место рождения и место смерти по форме: "Место рождения" "Место смерти"(Через пробел и без ковычек)')
    await state.set_state(StepsForms.GET_PLACE)

@router_callback.callback_query(F.data == "NOT_OK_DATE")
async def CallBackNotOkDate(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_DATE)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text("Укажите даты по форме: дд.мм.гг - дд.мм.гг (Между датами тире через пробел)")

'''
обработка коллбэков для пункта МЕСТО
'''
@router_callback.callback_query(F.data == 'OK_PLACE')
async def CallBackOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.update_data(PLACE = callback.message.text)
    await callback.answer('Продолжаем заполнение')
    await callback.message.answer('Напишите эпигроф для страницы памяти')
    await state.set_state(StepsForms.GET_EPIGRAPH)

@router_callback.callback_query(F.data == "NOT_OK_PLACE")
async def CallBackNotOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_PLACE)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text('Укажите место рождения и место смерти по форме: "Место рождения" "Место смерти"(Через пробел и без ковычек)')

'''
обработка коллбэков для пункта ЭПИГРОФ
'''
@router_callback.callback_query(F.data == 'OK_EPIGROPH')
async def CallBackOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.update_data(EPIGROPH = callback.message.text)
    await callback.answer('Продолжаем заполнение')
    await callback.message.answer('Напишите биографию для страницы памяти')
    await state.set_state(StepsForms.GET_BIOGRAPHY)

@router_callback.callback_query(F.data == "NOT_OK_EPIGROPH")
async def CallBackNotOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_EPIGRAPH)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text("Напишите эпигроф для страницы памяти")

'''
обработка коллбэков для пункта БИОГРАФИЯ
'''
@router_callback.callback_query(F.data == 'OK_BIOGRAPHY')
async def CallBackOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.update_data(BIOGRAPHY = callback.message.text)
    await callback.answer('Продолжаем заполнение')
    await state.set_state(StepsForms.FINISH)

@router_callback.callback_query(F.data == "NOT_OK_BIOGRAPHY")
async def CallBackNotOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_BIOGRAPHY)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text("Напишите биографию для страницы памяти")

'''
обработка событий для состояние ФИНИШ
'''
@router_callback.callback_query(F.data == 'OK_FINISH')
async def CallBackOkPlace(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Спасибо что воспользовались мной от AnkeBot")
    await callback.message.answer("Завершение заполнения анкеты")
     

@router_callback.callback_query(F.data == "NOT_OK_FINISH")
async def CallBackNotOkPlace(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_NAME_FOR_ANKET)
    await callback.answer("Заполняем это поле заново")
    await callback.message.edit_text("Укажите ФИО")

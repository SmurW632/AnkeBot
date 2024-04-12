#Форма заполнения анкеты пользователем без GPT
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from Forms.ViewForm.Keyboards.InlineKEyboards import *

router_form = Router()

class StepsForms(StatesGroup):
    '''
    Класс в котором лежат указатели состояния
    '''
    GET_NAME_FOR_ANKET = State()
    GET_PHOTO = State()
    GET_DATE = State()
    GET_PLACE = State()
    GET_EPIGRAPH = State()
    GET_BIOGRAPHY = State()
    GET_MEDIA = State()
    FINISH = State()



'''
Дальше идут обработчики которые направляются по событиям
'''
@router_form.message(Command('form'))
async def GetName(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, ("Укажите ФИО человека."))
    await message.delete()
    await state.update_data(ID_user = message.from_user.id) #айдишник пока берем из тг, потом переделать и присваивать свои айдишники
    await state.set_state(StepsForms.GET_NAME_FOR_ANKET)

@router_form.message(StepsForms.GET_NAME_FOR_ANKET)
async def SetName(message: Message):
    await message.answer(f"Провертье правильность заполнения данных:\n{message.text}", reply_markup = chek_name)

@router_form.message(StepsForms.GET_PHOTO)
async def SetPhoto(message: Message):
    await message.answer(f"Хотите оставить эту фотографию", reply_markup = chek_photo)

@router_form.message(StepsForms.GET_DATE)
async def SetDate(message: Message):
    await message.answer(f"Провертье правильность заполнения данных:\n {message.text}", reply_markup = chek_date)

@router_form.message(StepsForms.GET_PLACE)
async def SetPlace(message: Message, state: FSMContext):
    await message.answer(f"Провертье правильность заполнения данных:\n{message.text}", reply_markup = chek_place)

@router_form.message(StepsForms.GET_EPIGRAPH)
async def SetPlace(message: Message, state: FSMContext):
    await message.answer(f"Провертье правильность заполнения данных:\n{message.text}", reply_markup = chek_epigroph)

@router_form.message(StepsForms.GET_BIOGRAPHY)
async def SetPlace(message: Message, state: FSMContext):
    await message.answer(f"Провертье правильность заполнения данных:\n{message.text}", reply_markup = chek_biography)

@router_form.message(StepsForms.FINISH)
async def SetPlace(message: Message, state: FSMContext):
    data_state = await state.get_data()
    page_memory = f"""{data_state.get("FIO")}
{data_state.get("PHOTO")}
дата рождения и смерти: {data_state.get("DATE")}
место рождение и смерти: {data_state.get("PLACE")}
{data_state.get("EPIGROPH")}
{data_state.get("BIOGRAPHY")}
"""
    await message.answer(f"Вот ваша страница памяти: {page_memory}\n Хотите заполнить заново", reply_markup = chek_finish)
    await state.clear()
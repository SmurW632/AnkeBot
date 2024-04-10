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
    GET_BASE_INF = State()
    GET_AI_EPITAPHIA = State()
    GET_SHORT_INF = State()
    FINISH = State()

user_data = {
    "name": "Иванов Иван Иванович",
    "start": "",
    "end": "",
    "epitaph": "КРАТКАЯ ЭПИТАФИЯ",
    "author_epitaph": "АВТОР ЭПИТАФИИ", 
    "page_type_id": "1"
}

'''
Дальше идут обработчики которые направляются по событиям
'''
@router_form.message(Command('form'))
async def GetName(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, ("Укажите ФИО"))
    await message.delete()
    #await state.update_data(ID_user = message.from_user.id) #айдишник пока берем из тг, потом переделать и присваивать свои айдишники
    await state.set_state(StepsForms.GET_BASE_INF)

@router_form.message(StepsForms.GET_BASE_INF)
async def SetName(message: Message):
    await message.answer(f"Провертье правильность заполнения данных:\n{message.text}", reply_markup = chek_base_inf)

@router_form.message(StepsForms.GET_SHORT_INF)
async def SetDate(message: Message):
    await message.answer(f"Провертье правильность заполнения данных:\n {message.text}", reply_markup = chek_short_inf)

@router_form.message(StepsForms.GET_AI_EPITAPHIA)
async def SetPhoto(message: Message):
    await message.answer(f"Оставить эту эпитафию:\n{message.text}", reply_markup = chek_ai_ipitaphia)

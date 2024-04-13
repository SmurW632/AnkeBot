#Форма заполнения анкеты пользователем без GPT
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from Forms.ViewForm.Keyboards.InlineKEyboards import *
from app.Classactivity import *
import app.TranslateFun.TranslateFun as TF

router_form = Router()
'''data = FSMContext.get_data()
lang = data.get('lang',)'''
class StepsForms(StatesGroup):
    '''
    Класс в котором лежат указатели состояния
    '''
    GET_BASE_INF = State()
    GET_AI_EPITAPHIA = State()
    GET_SHORT_INF = State()
    FINISH = State()

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
@router_form.message(StepsLaunch.FORM)
async def SetName(message: Message):
    await message.answer(f"Оставить это ФИО:\n{message.text}", reply_markup = chek_base_inf)

@router_form.message(StepsForms.GET_SHORT_INF)
async def SetDate(message: Message):
    await message.answer(f"Оставить эти даты:\nДата рождения - {message.text.split(",")[0]}\nДата смерти - {message.text.split(",")[1]}", reply_markup = chek_short_inf)

@router_form.message(StepsForms.GET_AI_EPITAPHIA)
async def SetAiEpithap(message: Message):
    await message.answer(f"Оставить эту эпитафию:\n{message.text}", reply_markup = chek_ai_ipitaphia)
#Форма заполнения анкеты пользователем без GPT
from aiogram import Bot, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from Forms.ViewForm.Keyboards.InlineKEyboards import *
from app.Classactivity import *

router_form = Router()

class StepsForms(StatesGroup):
    
    # Класс в котором лежат указатели состояния
    
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

    # Дальше идут обработчики которые направляются по событиям

@router_form.message(StepsLaunch.FORM)
async def set_name(message: Message):
    user_data["name"] = message.text
    await message.answer(f"Оставьте это ФИО:\n{message.text}", reply_markup=chek_base_inf)

@router_form.message(StepsForms.GET_SHORT_INF)
async def set_date(message: Message):
    user_data["start"], user_data["end"] = message.text.split(",")
    await message.answer(f"Оставьте эти даты:\nДата рождения - {user_data['start']}\nДата смерти - {user_data['end']}", reply_markup=chek_short_inf)

@router_form.message(StepsForms.GET_AI_EPITAPHIA)
async def set_ai_epitaph(message: Message):
    user_data["epitaph"] = message.text
    await message.answer(f"Оставьте эту эпитафию:\n{message.text}", reply_markup=chek_ai_ipitaphia)
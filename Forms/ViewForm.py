#Форма заполнения анкеты пользователем без GPT

"""
1 шаг данные пользователя
2 шаг заполнение анкеты
"""
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class StepsForms(StatesGroup):
    GET_NAME_FOR_ANKET = State()
    GET_DATA = State()
    GET_PLACE = State()
    GET_EPIGRAPH = State()
    GET_BIOGRAPHY = State()
    GET_MEDIA = State()



async def GetName(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, ("Укажите ФИО человека."))
    await message.delete()
    await state.set_state(StepsForms.GET_NAME_FOR_ANKET)

async def SetName(message: Message, state: FSMContext):
    await state.update_data(FIO = message.text)
    await state.update_data(IDuser = message.from_user.id) #айдишник пока берем из тг, потом переделать
    await message.answer(f"Провертье правильность заполнения поля ФИО {message.text}")




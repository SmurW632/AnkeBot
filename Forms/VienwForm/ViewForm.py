#Форма заполнения анкеты пользователем без GPT
from app.Keyboard import Keyboard_chek
from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class StepsForms(StatesGroup):
    '''
    Класс в котором лежат указатели состояния
    '''
    GET_NAME_FOR_ANKET = State()
    GET_DATE = State()
    GET_PLACE = State()
    GET_EPIGRAPH = State()
    GET_BIOGRAPHY = State()
    GET_MEDIA = State()


'''
Дальше идут обработчики которые направляются по событиям
'''
async def GetName(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, ("Укажите ФИО человека."))
    await message.delete()
    await state.update_data(ID_user = message.from_user.id) #айдишник пока берем из тг, потом переделать и присваивать свои айдишники
    await state.set_state(StepsForms.GET_NAME_FOR_ANKET)

async def SetName(message: Message):
    await message.answer(f"Провертье правильность заполнения данных:\n{message.text}", reply_markup = Keyboard_chek())

async def CheckData(message: Message,bot: Bot, state: FSMContext):
    if message.text == 'Всё правильно':
        await state.update_data(FIO = message.text)
        await bot.send_message(message.from_user.id, "Введите даты жизни по образцу: дд.мм.гг-дд.мм.гг")
        await state.set_state(StepsForms.GET_DATE)
    else:
        await state.set_state(StepsForms.GET_NAME_FOR_ANKET)





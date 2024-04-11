#Форма заполнения анкеты пользователем без GPT
from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from Forms.VienwForm.Keyboards.InlineKEyboards import chek_data

router_form = Router()

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
@router_form.message(Command('viewform'))
async def GetName(message: Message, bot: Bot, state: FSMContext):
    await bot.send_message(message.from_user.id, ("Укажите ФИО человека."))
    await message.delete()
    await state.update_data(ID_user = message.from_user.id) #айдишник пока берем из тг, потом переделать и присваивать свои айдишники
    await state.set_state(StepsForms.GET_NAME_FOR_ANKET)

async def SetName(message: Message, state: FSMContext):
    await state.update_data(FIO = message.text)
    await message.answer(f"Провертье правильность заполнения данных:\n{message.text}", reply_markup = chek_data)






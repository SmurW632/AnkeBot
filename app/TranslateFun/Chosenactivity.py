
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import app.Keyboard as kb 
import app.TranslateFun.TranslateFun as TF
from app.Classactivity import *
from app.Handlers import *
router = Router()


@router.message(StepsForms.CHOSENACTIVITY)
async def choose_Activity(message: Message,state: FSMContext):
    data = await state.get_data()
    lang = await data.get('Lang', 'en')

    buttons = [
        [KeyboardButton(text=await TF.Translation("Начать заполнение",lang))],
        [KeyboardButton(text=await TF.Translation("Помочь с заполнением",lang))],
        [KeyboardButton(text=await TF.Translation("Помощь",lang))],
        [KeyboardButton(text=await TF.Translation("Обратная связь",lang))],
    ]

    buttonskb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,
                                            input_field_placeholder=await TF.Translation("Что будем делать?",lang))
    await message.answer(await TF.Translation("Что будем делать?",lang), reply_markup=buttonskb)


    if message.text in await TF.Translation("Начать заполнение",lang):
        pass

    elif message.text in await TF.Translation("Помочь с заполнением",lang):
        pass

    elif message.text in await TF.Translation("Помощь",lang):
        pass

    elif message.text in await TF.Translation("Обратная связь",lang):
        pass

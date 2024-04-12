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

@router.message(StepsForms.CHOSENLANGUAGE)

async def choose_language(message: Message,state: FSMContext):
    
    if message.text in "English 🇬🇧":
        lang = "en"
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        await state.update_data(lang=lang)
        buttons = [
            [KeyboardButton(text=await TF.Translation("Начать заполнение",lang))],
            [KeyboardButton(text=await TF.Translation("Помочь с заполнением",lang))],
            [KeyboardButton(text=await TF.Translation("Помощь",lang))],
            [KeyboardButton(text=await TF.Translation("Обратная связь",lang))],
        ]

        buttonskb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,
                                                input_field_placeholder=await TF.Translation("Что будем делать?",lang))
        await message.answer(await TF.Translation("Что будем делать?",lang), reply_markup=buttonskb)

        await state.set_state(StepsForms.CHOSENACTIVITY)

        # Добавляем пользователю атрибут английского языка в объект
    elif message.text in "Russian 🇷🇺":
        lang = 'ru'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        await state.update_data(lang=lang)
        buttons = [
            [KeyboardButton(text=await TF.Translation("Начать заполнение",lang))],
            [KeyboardButton(text=await TF.Translation("Помочь с заполнением",lang))],
            [KeyboardButton(text=await TF.Translation("Помощь",lang))],
            [KeyboardButton(text=await TF.Translation("Обратная связь",lang))],
        ]

        buttonskb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,
                                                input_field_placeholder=await TF.Translation("Что будем делать?",lang))
        await message.answer(await TF.Translation("Что будем делать?",lang), reply_markup=buttonskb)
        await state.set_state(StepsForms.CHOSENACTIVITY)
        # русский
    elif message.text in "Japanese 🇯🇵":
        lang = 'ja'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        await state.update_data(lang=lang)
        buttons = [
            [KeyboardButton(text=await TF.Translation("Начать заполнение",lang))],
            [KeyboardButton(text=await TF.Translation("Помочь с заполнением",lang))],
            [KeyboardButton(text=await TF.Translation("Помощь",lang))],
            [KeyboardButton(text=await TF.Translation("Обратная связь",lang))],
        ]

        buttonskb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,
                                                input_field_placeholder=await TF.Translation("Что будем делать?",lang))
        await message.answer(await TF.Translation("Что будем делать?",lang), reply_markup=buttonskb)
        await state.set_state(StepsForms.CHOSENACTIVITY)
        # анимешный
    elif message.text in "Chinese 🇨🇳":
        lang = 'zh-cn'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        await state.update_data(lang=lang)
        buttons = [
            [KeyboardButton(text=await TF.Translation("Начать заполнение",lang))],
            [KeyboardButton(text=await TF.Translation("Помочь с заполнением",lang))],
            [KeyboardButton(text=await TF.Translation("Помощь",lang))],
            [KeyboardButton(text=await TF.Translation("Обратная связь",lang))],
        ]

        buttonskb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,
                                                input_field_placeholder=await TF.Translation("Что будем делать?",lang))
        await message.answer(await TF.Translation("Что будем делать?",lang), reply_markup=buttonskb)
        await state.set_state(StepsForms.CHOSENACTIVITY)
        # китайский
    
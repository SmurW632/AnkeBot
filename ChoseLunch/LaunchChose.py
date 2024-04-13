from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

import app.TranslateFun.TranslateFun as TF
from app.Classactivity import *


router_launch = Router()
global lang 

languages = [
        [KeyboardButton(text="English 🇬🇧")],
        [KeyboardButton(text="Russian 🇷🇺")],
        [KeyboardButton(text="Japanese 🇯🇵")],
        [KeyboardButton(text="Chinese 🇨🇳")],
    ]
languagekb = ReplyKeyboardMarkup(keyboard=languages, resize_keyboard=True,
                                           input_field_placeholder="Choose your language")

@router_launch.message(CommandStart())
#async def cmd_start(message: Message):
#   await message.answer(f'Привет {message.from_user.first_name}.\nЯ бот по заполнению страницы памяти\nВыбери одну из функций.', reply_markup = MainMenu())
async def cmd_start(message: Message, state: FSMContext):
    await message.delete()
    await message.answer("Hello, setup my language!", reply_markup=languagekb)
    await state.set_state(StepsLaunch.CHOSENLANGUAGE)

@router_launch.message(StepsLaunch.CHOSENLANGUAGE)
async def choose_language(message: Message,state: FSMContext):
    if message.text == "English 🇬🇧":
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
        await state.set_state(StepsLaunch.CHOSENACTIVITY)

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
        await state.set_state(StepsLaunch.CHOSENACTIVITY)
        # русский

@router_launch.message(StepsLaunch.CHOSENACTIVITY)
async def perhod_activity(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('lang', 'en')
    if message.text in await TF.Translation("Начать заполнение",lang):
        await state.set_state(StepsLaunch.FORM)
        await bot.send_message(message.from_user.id, ("Укажите ФИО"))

    elif message.text in await TF.Translation("Помощь",lang):
        pass

    elif message.text in await TF.Translation("Обратная связь",lang):
        pass

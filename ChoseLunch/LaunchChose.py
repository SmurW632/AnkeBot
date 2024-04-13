from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

import app.TranslateFun.TranslateFun as TF
from app.Classactivity import *






router_launch = Router()
global lang 

@router_launch.message(CommandStart())
#async def cmd_start(message: Message):
#   await message.answer(f'Привет {message.from_user.first_name}.\nЯ бот по заполнению страницы памяти\nВыбери одну из функций.', reply_markup = MainMenu())
async def cmd_start(message: Message, state: FSMContext):

    languages = [
        [KeyboardButton(text="English 🇬🇧")],
        [KeyboardButton(text="Russian 🇷🇺")],
        [KeyboardButton(text="Japanese 🇯🇵")],
        [KeyboardButton(text="Chinese 🇨🇳")],
    ]
    languagekb = ReplyKeyboardMarkup(keyboard=languages, resize_keyboard=True,
                                           input_field_placeholder="Choose your language")
    
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
        await state.set_state(StepsLaunch.CHOSENACTIVITY)
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
        await state.set_state(StepsLaunch.CHOSENACTIVITY)
        # китайский

@router_launch.message(StepsLaunch.CHOSENACTIVITY)
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

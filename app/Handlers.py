from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.Keyboard as kb 

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    pass

    languages = [
        [KeyboardButton(text="English 🇬🇧")],
        [KeyboardButton(text="Russian 🇷🇺")],
        [KeyboardButton(text="Japanese 🇯🇵")],
        [KeyboardButton(text="Chinese 🇨🇳")],
    ]

    languagekb = ReplyKeyboardMarkup(keyboard=languages, resize_keyboard=True,
                                           input_field_placeholder="Choose your language")
    await message.answer("Hello, setup my language!", reply_markup=languagekb)

    @router.message()
    async def choose_language(message: Message):

        if message.text in "English":
            await message.answer("Вы успешно установили язык!")
            # Добавляем пользователю атрибут английского языка в объект
        elif message.text in "Russian":
            await message.answer("Вы успешно установили язык!")
            # русский
        elif message.text in "Japanese":
            await message.answer("Вы успешно установили язык!")
            # анимешный
        elif message.text in "Chinese":
            await message.answer("Вы успешно установили язык!")
            # китайский


@router.message()
async def choose_Activity(message: Message):
    
    buttons = [
        [KeyboardButton(text="Начать заполнение")],
        [KeyboardButton(text="Помочь с заполнением")],
        [KeyboardButton(text="Помощь")],
        [KeyboardButton(text="Обратная связь")],
    ]

    buttonskb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True,
                                            input_field_placeholder="What's shall we do?")
    await message.answer("What's shall we do?", reply_markup=buttonskb)

    if message.text in "Начать заполнение":
        pass

    elif message.text in "Помочь с заполнением":
        pass

    elif message.text in "Помощь":
        pass

    elif message.text in "Обратная связь":
        pass

    


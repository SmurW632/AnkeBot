from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove



from aiogram.fsm.context import FSMContext

import app.Classactivity
import app.Keyboard as kb 
import app.TranslateFun.TranslateFun as TF
import app.TranslateFun.Chosenactivity
import app.TranslateFun.Languagekeyboard
from app.Classactivity import *


router = Router()
global lang 

@router.message(CommandStart())
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


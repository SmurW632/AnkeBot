from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

import app.Classactivity
from app.Keyboard import MainMenu
import app.TranslateFun.TranslateFun as TF
import app.TranslateFun.Chosenactivity
import app.TranslateFun.Languagekeyboard
from app.Classactivity import *

router = Router()
global lang 

@router.message(CommandStart())
async def cmd_start(message: Message):
   await message.answer(f'Привет {message.from_user.first_name}.\nЯ бот по заполнению страницы памяти\nВыбери одну из функций.', reply_markup = MainMenu())
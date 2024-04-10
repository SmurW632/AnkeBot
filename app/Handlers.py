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
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}')


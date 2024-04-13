from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from app.Keyboard import MainMenu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.first_name}.\nЯ бот по заполнению страницы памяти\nВыбери одну из функций.', reply_markup = MainMenu())



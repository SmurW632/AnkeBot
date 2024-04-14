from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from Keyboards.InlineKeyboard import *
from Classes.BotClasses import *
from ClientRequests.api_requests import *
import Translate.FuncTranslate as TF


router_request = Router()

user_data_auth = {
        "email": 'email',
        "password": 'password',
        "device": '2123'
}

@router_request.message(StepsBots.AUTORIZATION)
async def GetMail(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', 'en')
    user_data_auth['email'] = message.text
    await bot.send_message(message.from_user.id, await TF.Translation("Введите свой пароль", lang))
    await state.set_state(StepsBots.GET_PASSWORD)

@router_request.message(StepsBots.GET_PASSWORD)
async def GetPassword(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', 'en')
    buttons = [
            [KeyboardButton(text=await TF.Translation("Начать заполнение", lang))],
            [KeyboardButton(text=await TF.Translation("Заполнить голосом", lang))],
            [KeyboardButton(text=await TF.Translation("Скан фото", lang))],
            [KeyboardButton(text=await TF.Translation("Помощь", lang))]
        ]
        
    buttonskb = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, input_field_placeholder=await TF.Translation("Что будем делать?", lang))

    user_data_auth['password'] = message.text
    if await get_access_token(user_data_auth['email'], user_data_auth['password'], user_data_auth['device']) != None:
        await bot.send_message(message.from_user.id, await TF.Translation('Вы успешно авторизовались\nЧто хотите сделать?', lang), reply_markup = buttonskb)
        await state.set_state(StepsBots.CHOSENACTIVITY)
    else:
        await bot.send_message(message.from_user.id, await TF.Translation('Что то пошло не так, попробуйте еще раз.\nВедите свой емэйл.', lang))

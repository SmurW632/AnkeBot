from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class StepsForms(StatesGroup):
    '''
    Класс в котором лежат указатели состояния
    '''
    CHOSENLANGUAGE = State()
    CHOSENACTIVITY = State()

import app.Keyboard as kb 
import app.TranslateFun.TranslateFun as TF
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
    await state.set_state(StepsForms.CHOSENLANGUAGE)

@router.message(StepsForms.CHOSENLANGUAGE)

async def choose_language(message: Message,state: FSMContext):
    
    if message.text in "English 🇬🇧":
        lang = "en"
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        
        # Добавляем пользователю атрибут английского языка в объект
    elif message.text in "Russian 🇷🇺":
        lang = 'ru'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        # русский
    elif message.text in "Japanese 🇯🇵":
        lang = 'ja'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        # анимешный
    elif message.text in "Chinese 🇨🇳":
        lang = 'zh-cn'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        # китайский
    await state.update_data(lang=lang)
    await state.set_state(StepsForms.CHOSENACTIVITY)


@router.message(StepsForms.CHOSENACTIVITY)
async def choose_Activity(message: Message,state: FSMContext):
    data = await state.get_data()
    lang = await data.get('lang', 'en')

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

    


from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

import Translate.FuncTranslate as TF
from Keyboards.ReplyKeyboard import *
from Classes.BotClasses import *


router_start = Router()


@router_start.message(CommandStart())
#async def cmd_start(message: Message):
#   await message.answer(f'Привет {message.from_user.first_name}.\nЯ бот по заполнению страницы памяти\nВыбери одну из функций.', reply_markup = MainMenu())
async def cmd_start(message: Message, state: FSMContext):
    await message.delete()
    await message.answer("Hello, setup my language!", reply_markup=languagekb)
    await state.set_state(StepsBots.CHOSENLANGUAGE)

@router_start.message(StepsBots.CHOSENLANGUAGE)
async def choose_language(message: Message,state: FSMContext):
    if message.text == "English 🇬🇧":
        lang = 'en'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        await state.update_data(Lang = lang)
        await message.answer(await TF.Translation("А теперь необходимо авторизоваться\nВведите емэйл", lang))
        await state.set_state(StepsBots.AUTORIZATION)

        # Добавляем пользователю атрибут английского языка в объект
    elif message.text in "Russian 🇷🇺":
        lang = 'ru'
        await message.answer(await TF.Translation("Вы успешно установили язык!",lang),reply_markup=ReplyKeyboardRemove())
        await state.update_data(Lang = lang)
        await message.answer(await TF.Translation("А теперь необходимо авторизоваться\nВведите емэйл",lang))
        await state.set_state(StepsBots.AUTORIZATION)
        # русский

@router_start.message(StepsBots.CHOSENACTIVITY)
async def perhod_activity(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang', 'en')
    if message.text in await TF.Translation("Начать заполнение", lang):
        await message.delete()
        await state.set_state(StepsBots.FORM)
        await bot.send_message(message.from_user.id, await TF.Translation("Укажите ФИО", lang), reply_markup=ReplyKeyboardRemove())


    elif message.text in await TF.Translation("Помощь", lang):
        await message.delete()
        await message.answer(f'''{await TF.Translation("Привет", lang)} {message.from_user.first_name}.
{await TF.Translation("Я бот по заполнению страницы памяти.", lang)}
{await TF.Translation("Что я могу:", lang)}
{await TF.Translation("Я могу заполнить форму используя Yandex GPT для полей эпитафия и биография;", lang)}
{await TF.Translation("Так же могу сканировать твое изображение и заполнить некоторые поля автоматически (в разработке);", lang)}
{await TF.Translation("Еще могу заполнять поля по вашим голосовым сообщениям (в разработке). ", lang)}''')
    
    elif message.text in await TF.Translation("Заполнить голосом",lang):
        await message.delete()
        await bot.send_message(message.from_user.id, await TF.Translation("Пришли гололсовое сообщения для его распознования.", lang))
        await state.set_state(StepsBots.READER_VOICE)
        
    elif message.text in await TF.Translation("Сканирование",lang):
        await message.delete()
        await message.answer(await TF.Translation("Пожалуйста, пришлите фото с информацией." , lang))
        await message.answer(await TF.Translation("Постарайтесь, чтобы текст было хорошо видно.", lang))
        await state.set_state(StepsBots.READER_PHOTO)
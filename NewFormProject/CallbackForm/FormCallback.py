#Здесь будут храниться колл бэки клавиатуры для формы заполнения анкеты без GPT
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import Translate.FuncTranslate as TF
from Classes.BotClasses import *
from Form.HandlersForm import user_data
from Keyboards.InlineKeyboard import *
from GPTReauests.RequestsGPT import prompt
from Data.SaveJsonUserData import save_user_data
from ClientRequests.api_requests import *

router_callback = Router()


@router_callback.callback_query(F.data == 'EDIT_FIO')
async def EditName(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    await callback.message.edit_text(await TF.Translation("Напишите новое ФИО.", lang))
    await state.set_state(StepsEdit.EDIT_FIO)

@router_callback.callback_query(F.data == 'EDIT_DATE_B')
async def EditDateB(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    await callback.message.edit_text(await TF.Translation("Напишите дату рождения.", lang))
    await state.set_state(StepsEdit.EDIT_DATE_B)

@router_callback.callback_query(F.data == 'EDIT_DATE_D')
async def EditDateD(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    await callback.message.edit_text(await TF.Translation("Напишите дату смерти.", lang))
    await state.set_state(StepsEdit.EDIT_DATE_D)

@router_callback.callback_query(F.data == 'EPITAPH')
async def EditEpitaph(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lang = data.get('Lang')
    await callback.message.edit_text(await TF.Translation("Напишите краткую информацию о человеке.\nНапример Место рождение, место смерти, супруги, дети, достижения, деятельность и т.п\nЧем больше информации тем лучше будет ответ от Yandex GPT.", lang))
    await state.set_state(StepsEdit.EPITAPH)
    



@router_callback.callback_query(F.data == 'END')
async def END(callback: CallbackQuery, state: FSMContext):
    await update_memory_page(callback.message)


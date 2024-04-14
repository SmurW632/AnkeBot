#Здесь будут храниться колл бэки клавиатуры для формы заполнения анкеты без GPT
from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import Translate.FuncTranslate as TF
from Classes.BotClasses import StepsForms
from Form.HandlersForm import user_data
from Keyboards.InlineKeyboard import *
from GPTReauests.RequestsGPT import prompt
from Data.SaveJsonUserData import save_user_data
from ClientRequests.api_requests import update_memory_page

router_callback = Router()

@router_callback.callback_query(F.data == 'END')
async def END(callback: CallbackQuery, state: FSMContext):
    await update_memory_page(callback.message)
   

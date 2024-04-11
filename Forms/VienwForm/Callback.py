#Здесь будут храниться колл бэки клавиатуры для формы заполнения анкеты без GPT
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

router_callback = Router()

@router_callback.callback_query(F.data == 'OK')
async def CallBackOK(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Продолжаем заполнение')

@router_callback.callback_query(F.data == "NOT OK")
async def CallBackNoOk(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Заполняем это поле заново")
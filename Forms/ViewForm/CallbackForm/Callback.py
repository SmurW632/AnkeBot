from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from Forms.ViewForm.ViewFormNoGPT import StepsForms, user_data
from Forms.ViewForm.Keyboards.InlineKEyboards import *
from Forms.GPTRequest.RequestGPT import prompt
from Forms.Save_user_data_in_json import save_user_data

router_callback = Router()

async def handle_not_ok_base_inf(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_BASE_INF)
    await callback.answer()
    await callback.message.edit_text("Укажите ФИО")
    
async def handle_ok_base_inf(callback: CallbackQuery, state: FSMContext):
    user_data["name"] = callback.message.text
    await callback.answer()
    await callback.message.edit_text('Укажите дату рождения, дату смерти. Запишите через запятую')
    await state.set_state(StepsForms.GET_SHORT_INF)

async def handle_ok_short_inf(callback: CallbackQuery, state: FSMContext):
    answer_user = callback.message.text.split(',')
    print(answer_user)
    await callback.answer()
    await callback.message.edit_text("Напишите запрос для составления эпитафии")
    await state.set_state(StepsForms.GET_AI_EPITAPHIA)

async def handle_not_ok_short_inf(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_SHORT_INF)
    await callback.answer()
    await callback.message.edit_text("Укажите дату рождения, дату смерти. Запишите через запятую")
    
async def handle_ok_ai_epitaphia(callback: CallbackQuery, state: FSMContext):
    answer_GPT = await prompt(callback.message.text + 'Напиши эпитафию для страницы памяти о человеке на основе этого текста. Так же в отдельном предложении укажи автора эпитафии.')
    await callback.answer('завершение заполнения')
    await callback.message.edit_text(f'Вот эпитафия по вашему запросу:\n{answer_GPT}')
    await state.set_state(StepsForms.FINISH)
    print(answer_GPT)

async def handle_not_ok_ai_epitaphia(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_AI_EPITAPHIA)
    await callback.answer()
    await callback.message.edit_text("Напишите какую эпитафию вы хотите или автора эпитафии")

async def handle_ok_finish(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Спасибо что воспользовались мной от AnkeBot")
    await callback.message.answer("Вот ваша ссылка на страницу памяти")

async def handle_not_ok_finish(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StepsForms.GET_BASE_INF)
    await callback.answer("Заполняем данные заново")
    await callback.message.edit_text("Укажите ФИО")
    

@router_callback.callback_query(F.data == 'OK_BASE_INF')
async def callback_ok_base_inf_handler(callback: CallbackQuery, state: FSMContext):
    await handle_ok_base_inf(callback, state)

@router_callback.callback_query(F.data == "NOT_OK_BASE_INF")
async def callback_not_ok_base_inf_handler(callback: CallbackQuery, state: FSMContext):
    await handle_not_ok_base_inf(callback, state)

@router_callback.callback_query(F.data == 'OK_SHORT_INF')
async def callback_ok_short_inf_handler(callback: CallbackQuery, state: FSMContext):
    await handle_ok_short_inf(callback, state)

@router_callback.callback_query(F.data == "NOT_OK_SHORT_INF")
async def callback_not_ok_short_inf_handler(callback: CallbackQuery, state: FSMContext):
    await handle_not_ok_short_inf(callback, state)

@router_callback.callback_query(F.data == 'OK_AI_IPITAPHIA')
async def callback_ok_ai_epitaphia_handler(callback: CallbackQuery, state: FSMContext):
    await handle_ok_ai_epitaphia(callback, state)

@router_callback.callback_query(F.data == "NOT_OK_AI_IPITAPHIA")
async def callback_not_ok_ai_epitaphia_handler(callback: CallbackQuery, state: FSMContext):
    await handle_not_ok_ai_epitaphia(callback, state)

@router_callback.callback_query(F.data == 'OK_FINISH')
async def callback_ok_finish_handler(callback: CallbackQuery, state: FSMContext):
    await handle_ok_finish(callback, state)

@router_callback.callback_query(F.data == "NOT_OK_FINISH")
async def callback_not_ok_finish_handler(callback: CallbackQuery, state: FSMContext):
    await handle_not_ok_finish(callback, state)


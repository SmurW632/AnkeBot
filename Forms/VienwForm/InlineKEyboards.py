from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

chek_data = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'Все правильно', callback_data = 'OK'), 
        InlineKeyboardButton(text = "Заполнить заново", callback_data = "NOT OK")
    ]
])


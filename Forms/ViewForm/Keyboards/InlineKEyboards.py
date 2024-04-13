from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

chek_base_inf = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = '👍', callback_data = 'OK_BASE_INF'), 
        InlineKeyboardButton(text = "👎", callback_data = "NOT_OK_BASE_INF")
    ]
])

chek_ai_ipitaphia = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = '👍', callback_data = 'OK_AI_IPITAPHIA'), 
        InlineKeyboardButton(text = "👎", callback_data = "NOT_OK_AI_IPITAPHIA")
    ]
])

chek_short_inf = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = '👍', callback_data = 'OK_SHORT_INF'), 
        InlineKeyboardButton(text = "👎", callback_data = "NOT_OK_SHORT_INF")
    ]
])


chek_finish = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = '👍', callback_data = 'OK_FINISH'), 
        InlineKeyboardButton(text = "👎", callback_data = "NOT_OK_FINISH")
    ]
])
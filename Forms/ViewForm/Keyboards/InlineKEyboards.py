from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)

chek_name = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'Все правильно', callback_data = 'OK_NAME'), 
        InlineKeyboardButton(text = "Заполнить заново", callback_data = "NOT_OK_NAME")
    ]
])

chek_photo = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'ДА', callback_data = 'OK_PHOTO'), 
        InlineKeyboardButton(text = "НЕТ", callback_data = "NOT_OK_PHOTO")
    ]
])

chek_date = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'Все правильно', callback_data = 'OK_DATE'), 
        InlineKeyboardButton(text = "Заполнить заново", callback_data = "NOT_OK_DATE")
    ]
])

chek_place = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'Все правильно', callback_data = 'OK_PLACE'), 
        InlineKeyboardButton(text = "Заполнить заново", callback_data = "NOT_OK_PLACE")
    ]
])

chek_epigroph = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'Все правильно', callback_data = 'OK_EPIGROPH'), 
        InlineKeyboardButton(text = "Заполнить заново", callback_data = "NOT_OK_EPIGROPH")
    ]
])

chek_biography = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'Все правильно', callback_data = 'OK_BIOGRAPHY'), 
        InlineKeyboardButton(text = "Заполнить заново", callback_data = "NOT_OK_BIOGRAPHY")
    ]
])

chek_finish = InlineKeyboardMarkup(inline_keyboard = [
    [
        InlineKeyboardButton(text = 'Нет, хочу закончить заполнение', callback_data = 'OK_FINISH'), 
        InlineKeyboardButton(text = "Заполнить заново", callback_data = "NOT_OK_FINISH")
    ]
])
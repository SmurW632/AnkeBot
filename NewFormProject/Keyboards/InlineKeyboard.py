from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

edit_inf_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = f"ФИО", callback_data='EDIT_FIO'),
            InlineKeyboardButton(text = f"Дату рождения", callback_data='EDIT_DATE_B'),
        ],
        [
            InlineKeyboardButton(text = f"Дату смерти", callback_data='EDIT_DATE_D'),
            InlineKeyboardButton(text = f"Эпитафию", callback_data='EPITAPH'),
        ],
        [
            InlineKeyboardButton(text = f"Биографию", callback_data='BIOGRAPH'),
            InlineKeyboardButton(text = f"Закончить", callback_data='END')
        ]
    ]
)

edit_inf_en = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = f"Name", callback_data='EDIT_FIO'),
            InlineKeyboardButton(text = f"Date of birth", callback_data='EDIT_DATE_B'),
        ],
        [
            InlineKeyboardButton(text = f"Date of death", callback_data='EDIT_DATE_D'),
            InlineKeyboardButton(text = f"The epitaph", callback_data='EPITAPH'),
        ],
        [
            InlineKeyboardButton(text = f"Biography", callback_data='BIOGRAPH'),
            InlineKeyboardButton(text = f"To finish", callback_data='END')
        ]
    ]
)

photo_like = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = f"👍", callback_data='OK'),
            InlineKeyboardButton(text = f"👎", callback_data='NOT_OK'),
        ]
    ]
)

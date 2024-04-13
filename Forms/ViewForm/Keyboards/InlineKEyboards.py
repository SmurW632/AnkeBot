from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_inline_keyboard(callback_data_prefix):
    return InlineKeyboardMarkup(inline_keyboard = [
        [
            InlineKeyboardButton(text = '👍', callback_data = f'OK_{callback_data_prefix}'), 
            InlineKeyboardButton(text = '👎', callback_data = f'NOT_OK_{callback_data_prefix}')
        ]
    ])

chek_base_inf = create_inline_keyboard('BASE_INF')
chek_ai_ipitaphia = create_inline_keyboard('AI_IPITAPHIA')
chek_short_inf = create_inline_keyboard('SHORT_INF')
chek_finish = create_inline_keyboard('FINISH')
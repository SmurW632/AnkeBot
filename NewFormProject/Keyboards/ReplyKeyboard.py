from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

languages = [
        [KeyboardButton(text="English 🇬🇧")],
        [KeyboardButton(text="Russian 🇷🇺")]
    ]
languagekb = ReplyKeyboardMarkup(keyboard=languages, resize_keyboard=True,
                                           input_field_placeholder="Choose your language")
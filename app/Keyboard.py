from aiogram.utils.keyboard import ReplyKeyboardBuilder

def MainMenu():
    main_menu = ReplyKeyboardBuilder()
    main_menu.button(text = 'Заполнить страницу памяти')
    main_menu.button(text = 'Скан фото')
    main_menu.button(text = 'Помощь')
    main_menu.adjust(1, 2)
    return main_menu.as_markup(resize_keyboard = True)
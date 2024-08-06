from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class Buttons: 
    menu_button = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Корзина 🛒')],
                                        [KeyboardButton(text='Информация о нас 📃✏️'), KeyboardButton(text='Контакт 📰')]],
            resize_keyboard=True,
            input_field_placeholder='Выберите пунт меню.')
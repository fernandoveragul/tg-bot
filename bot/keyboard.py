from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn_main = InlineKeyboardButton('🧊Основное🔥', callback_data='btn_main')
btn_wind = InlineKeyboardButton('🌬️ Что по ветру?', callback_data='btn_wind')
btn_sun = InlineKeyboardButton('☀️Во сколько восход?\nА закат?🌑', callback_data='btn_sun')

buttons = [
    [btn_main],
    [btn_wind],
    [btn_sun]
]
keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

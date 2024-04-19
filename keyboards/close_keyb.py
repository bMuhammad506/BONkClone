from callbackdata.callback_data import basic_btn
from aiogram.utils.keyboard import InlineKeyboardBuilder


def close_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text = "Close", callback_data=basic_btn(data = "close").pack()),
    return builder.as_markup()
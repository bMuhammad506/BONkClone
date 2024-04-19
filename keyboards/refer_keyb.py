from callbackdata.callback_data import basic_btn
from aiogram.utils.keyboard import InlineKeyboardBuilder


def refer_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text = "Close", callback_data=basic_btn(data = "close").pack())
    builder.button(text = "Generate QR", callback_data=basic_btn(data = "qr").pack())
    return builder.as_markup()
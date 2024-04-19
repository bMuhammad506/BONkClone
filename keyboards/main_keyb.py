from callbackdata.callback_data import basic_btn
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_keyboard():
    builder = InlineKeyboardBuilder()
    
    builder.button(text = "Buy", callback_data=basic_btn(data = "buy").pack())
    builder.button(text = "Sell & Manage", callback_data=basic_btn(data = "sellmng").pack())
    builder.button(text = "Help", callback_data=basic_btn(data = "help").pack())
    builder.button(text = "Refer Friends", callback_data=basic_btn(data = "refer").pack())
    builder.button(text = "Alerts", callback_data=basic_btn(data = "alert").pack())
    builder.button(text = "Wallet", callback_data=basic_btn(data = "wallet").pack())
    builder.button(text = "Settings", callback_data=basic_btn(data = "settings").pack())
    builder.button(text = "Pin", callback_data=basic_btn(data = "pin").pack())
    builder.button(text = "Refresh", callback_data=basic_btn(data = "refreshmain").pack())
    
    builder.adjust(2,3,2,2)


    return builder.as_markup()
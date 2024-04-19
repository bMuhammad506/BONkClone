from callbackdata.callback_data import basic_btn
from aiogram.utils.keyboard import InlineKeyboardBuilder


def wallet_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text = "View on Solscan", callback_data=basic_btn(data = "scan").pack())
    builder.button(text = "Close", callback_data=basic_btn(data = "closewallet").pack())
    builder.button(text = "Deposit Sol", callback_data=basic_btn(data = "deposit").pack())
    builder.button(text = "Withdraw all Sol", callback_data=basic_btn(data = "withdraw").pack())
    builder.button(text = "Withdraw X Sol", callback_data=basic_btn(data = "withdrawX").pack())
    builder.button(text = "Reset Wallet", callback_data=basic_btn(data = "reset").pack())
    builder.button(text = "Export Private Key", callback_data=basic_btn(data = "export").pack())
    builder.button(text = "Refresh", callback_data=basic_btn(data = "refreshwallet").pack())

    builder.adjust(2,1,2,2,1)

    return builder.as_markup()

def resetconfirmation_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text = "Confirm", callback_data=basic_btn(data = "confirm").pack())
    builder.button(text = "Cancel", callback_data=basic_btn(data = "cancel").pack())
   
    builder.adjust(2)

    return builder.as_markup()

def exportconfirmation_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text = "Confirm", callback_data=basic_btn(data = "confirmExport").pack())
    builder.button(text = "Cancel", callback_data=basic_btn(data = "cancelExport").pack())
   
    builder.adjust(2)

    return builder.as_markup()
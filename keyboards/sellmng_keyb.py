from callbackdata.callback_data import sell_btn, basic_btn, mng_btn
from aiogram.utils.keyboard import InlineKeyboardBuilder

def sellmng_keyboard(res):
    builder = InlineKeyboardBuilder()
    count = 1

    if(res):
        for i in res:
            builder.button(text = f"{i.tok_address}", callback_data=basic_btn(data="onlyfortext"))
            builder.button(text = f"Sell", callback_data=sell_btn(data = i.tok_address).pack())
            builder.button(text = f"Manage", callback_data=mng_btn(data = i.tok_address).pack())
    
    builder.button(text = "Close", callback_data=basic_btn(data = "close").pack())
    builder.adjust(1,2,repeat=True)
    
    return builder.as_markup()
from callbackdata.callback_data import basic_btn
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from db.dbhandler import readUser

async def setting_keyboard():
    builder = InlineKeyboardBuilder()
    user = await readUser()

    pencil = '\U0000270E'
    red_button = '\U0001F534'
    green_button = '\U0001F7E2'

    builder.button(text = "---General Settings---", callback_data=basic_btn(data = "genset").pack())
    if(user.user_announcement == 0):
        builder.button(text = f"{red_button} Anouncements", callback_data=basic_btn(data = "disableclick").pack())
    else:
        builder.button(text = f"{green_button} Anouncements", callback_data=basic_btn(data = "enableclick").pack())
    builder.button(text = f"{pencil} Min Pos Value : ${user.min_pos_value}", callback_data=basic_btn(data = "editpos").pack())

    builder.button(text = "---Slippage Config---", callback_data=basic_btn(data = "slpconfig").pack())
    builder.button(text = f"{pencil} Buy : %{user.slippage_buy}", callback_data=basic_btn(data = "editslpbuy").pack())
    builder.button(text = f"{pencil} Sell : %{user.slippage_sell}", callback_data=basic_btn(data = "editslpsell").pack())


    builder.button(text = " Refresh ", callback_data=basic_btn(data = "refreshsettings").pack())
    builder.button(text = " Close ", callback_data=basic_btn(data = "closesettings").pack())
    
    builder.adjust(1,2,1,2,2)


    return builder.as_markup()
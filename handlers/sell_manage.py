from aiogram import F, Router
from callbackdata.callback_data import basic_btn, sell_btn
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.sellmng_keyb import sellmng_keyboard
from db.dbhandler import readToken, deleteToken

sellmng_rt = Router()

@sellmng_rt.callback_query(basic_btn.filter(F.data=="sellmng"))
async def sellmng(call: CallbackQuery, state : FSMContext):
    results = await readToken()
    inline_keyboard = sellmng_keyboard(results)
    i = 1
    if(results):
        text_1="Following are your Tokens"
    else:
        text_1="No Tokens to show"
    await call.message.reply(text=text_1, reply_markup=inline_keyboard)


@sellmng_rt.callback_query(sell_btn.filter())
async def selltoken(call : CallbackQuery, state: FSMContext):
    data_list = call.data.split(":")
    data = data_list[1]
    await deleteToken(data)
    await call.message.answer("Token deleted Close and Open again")
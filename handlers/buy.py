from aiogram import F, Router, types
from keyboards.close_keyb import close_keyboard 
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from FSM.states import InputState
from db.dbhandler import createToken

buy_rt = Router()

@buy_rt.callback_query(basic_btn.filter(F.data=="buy"))
async def buy(call: CallbackQuery, state : FSMContext):
    inline_keyboard = close_keyboard()
    await state.set_state(InputState.waiting_for_tok_address)
    await call.message.reply("Enter the token Address.", reply_markup = inline_keyboard)

@buy_rt.message(InputState.waiting_for_tok_address)
async def token_bought(message: types.message, state:FSMContext):
    await createToken(message.text)
    await message.answer('Token Bought')
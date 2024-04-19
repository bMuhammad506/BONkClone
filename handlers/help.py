from aiogram import F, Router
from keyboards.close_keyb import close_keyboard 
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from FSM.states import InputState

help_rt = Router()

@help_rt.callback_query(basic_btn.filter(F.data=="help"))
async def help(call: CallbackQuery, state : FSMContext):
    inline_keyboard = close_keyboard()
    await state.set_state(InputState.waiting_for_tok_address)
    await call.message.reply("""Help:
  
    Which tokens can I trade?
    Any SPL token that is a Sol pair, on Raydium, Orca, and Jupiter. We pick up raydium pairs instantly, and Jupiter will pick up non sol pairs within around 15 minutes

    How can I see how much money I've made from referrals?
    Check the referrals button or type /referrals to see your payment in Bonk!""", reply_markup = inline_keyboard)
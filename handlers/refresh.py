from aiogram import Router, F
from keyboards.main_keyb import main_keyboard
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery
from db.dbhandler import readUser

refresh_rt = Router()

@refresh_rt.callback_query(basic_btn.filter(F.data=="refreshmain"))
async def st_funct(call : CallbackQuery):
    inline_keyboard = main_keyboard()
    user = await readUser()
    await call.message.edit_text(f"Hello! I'm your Solana bot.\n Your balance is : {user.user_balance}", reply_markup = inline_keyboard)
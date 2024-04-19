from aiogram import F, Router
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery

pin_rt = Router()

@pin_rt.callback_query(basic_btn.filter(F.data=="pin"))
async def pinmain(call: CallbackQuery):
    await call.message.chat.pin_message(call.message.message_id)
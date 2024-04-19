from aiogram import F, Router
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery

close_rt = Router()

@close_rt.callback_query(basic_btn.filter(F.data=="close"))
async def close(call: CallbackQuery):
    await call.message.delete()
# Event Handler which process the request when someone clicks on alerts button on keyboard
# should redirect the user to the announcement groups on telegram

from aiogram import F, Router
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery

alert_rt = Router()

@alert_rt.callback_query(basic_btn.filter(F.data=="alert"))
async def buy(call: CallbackQuery):
    await call.message.answer("Alert Event Handled")
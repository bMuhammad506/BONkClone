from aiogram import F, Router, types
from keyboards.settings_keyb import setting_keyboard
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery, ForceReply
from aiogram.fsm.context import FSMContext
from FSM.states import InputState
from db.dbhandler import updateUser

settings_rt = Router()

@settings_rt.callback_query(basic_btn.filter(F.data=="settings"))
async def setting(call: CallbackQuery):
    inline_keyboard = await setting_keyboard()
    await call.message.reply("Welcome to settings", reply_markup = inline_keyboard)

@settings_rt.callback_query(basic_btn.filter(F.data=="disableclick"))
async def enableanounce(call: CallbackQuery):
    await updateUser(user_announcement= True)
    inline_keyboard = await setting_keyboard()
    await call.message.edit_reply_markup(reply_markup = inline_keyboard)

@settings_rt.callback_query(basic_btn.filter(F.data=="enableclick"))
async def disableannounce(call: CallbackQuery):
    await updateUser(user_announcement= False)
    inline_keyboard = await setting_keyboard()
    await call.message.edit_reply_markup(reply_markup = inline_keyboard)

@settings_rt.callback_query(basic_btn.filter(F.data=="editpos"))
async def editposvalue(call: CallbackQuery, state: FSMContext):
    reply = ForceReply()
    await state.set_state(InputState.get_pos_value)
    await call.message.answer(text = "Send your new POS value", reply_markup=reply)

@settings_rt.message(InputState.get_pos_value)
async def setnewPOS(message: types.message):
    await updateUser(min_pos_value= float(message.text))
    await message.answer("POS value updated Please Refresh")

@settings_rt.callback_query(basic_btn.filter(F.data=="refreshsettings"))
async def refresh(call: CallbackQuery):
    inline_keyboard = await setting_keyboard()
    await call.message.edit_text("Welcome to settings", reply_markup = inline_keyboard)

@settings_rt.callback_query(basic_btn.filter(F.data=="editslpbuy"))
async def forcenewslpbuy(call: CallbackQuery, state: FSMContext):
    reply = ForceReply()
    await state.set_state(InputState.get_slpbuy)
    await call.message.answer(text = "Send your new slippage buy value", reply_markup=reply)

@settings_rt.message(InputState.get_slpbuy)
async def setnewslpbuy(message: types.message):
    await updateUser(slippage_buy = int(message.text))
    await message.answer("SLIPPAGE BUY value updated Please Refresh")

@settings_rt.callback_query(basic_btn.filter(F.data=="editslpsell"))
async def forcenewslpsell(call: CallbackQuery, state: FSMContext):
    reply = ForceReply()
    await state.set_state(InputState.get_slpsell)
    await call.message.answer(text = "Send your new slippage sell value", reply_markup=reply)

@settings_rt.message(InputState.get_slpsell)
async def setnewslpsell(message: types.message):
    await updateUser(slippage_sell=int(message.text))
    await message.answer("SLIPPAGE sell value updated Please Refresh")

@settings_rt.callback_query(basic_btn.filter(F.data=="closesettings"))
async def close(call: CallbackQuery):
    await call.message.delete()


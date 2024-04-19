from aiogram import F, Router, types
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery
from db.dbhandler import updateUser, deleteUser, createUser, readUser
from keyboards.wallet_keyb import wallet_keyboard, resetconfirmation_keyboard, exportconfirmation_keyboard
from aiogram.fsm.context import FSMContext
from FSM.states import InputState
import os
import asyncio

wallet_rt = Router()

@wallet_rt.callback_query(basic_btn.filter(F.data=="wallet"))
async def walletstart(call: CallbackQuery):
    user = await readUser()
    print(f"\n-----------------------------------------------------------------------------------------------------\n{user}\n-----------------------------------------------------------------------------------------------------------------------\n")
    inline_keyboard = wallet_keyboard()
    await call.message.reply(f"Address: {user.user_address} \nBalance: {user.user_balance}", reply_markup = inline_keyboard)

@wallet_rt.callback_query(basic_btn.filter(F.data=="closewallet"))
async def closewallet(call: CallbackQuery):
    await call.message.delete()

@wallet_rt.callback_query(basic_btn.filter(F.data=="deposit"))
async def deposit(call: CallbackQuery, state: FSMContext):
    user = await readUser()
    await call.message.answer("To Deposit, send SOL to followong address;")
    await call.message.answer(f"{user.user_address}")

@wallet_rt.callback_query(basic_btn.filter(F.data=="withdraw"))
async def withdraw(call: CallbackQuery):
    user = await readUser()
    if(user.user_balance <= 0):
        await call.message.answer("Not enough SOL to withdraw")
    else:
        await updateUser(user_balance=0.0)
        await call.message.answer("Sol Withdrawn")

@wallet_rt.callback_query(basic_btn.filter(F.data=="withdrawX"))
async def getwithdrawValue(call: CallbackQuery, state:FSMContext):
    user = await readUser()
    if(user.user_balance <= 0):
        await call.message.answer("Not enough SOL to withdraw")
    else:
        await call.message.answer("Enter amount to withdraw")
        await state.set_state(InputState.waiting_for_userSolValue)

@wallet_rt.message(InputState.waiting_for_userSolValue)
async def withdrawX(message: types.message):
    user = await readUser()
    await updateUser(user_balance=user.user_balance - float(message.text))
    await message.answer(f"Your remaining balance is : {user.user_balance}")


@wallet_rt.callback_query(basic_btn.filter(F.data=="reset"))
async def resetConfirmation(call: CallbackQuery):
    inline_keyboard = resetconfirmation_keyboard()
    await call.message.reply("Are you sure you want to reset this wallet and create a new one ?", reply_markup = inline_keyboard)

@wallet_rt.callback_query(basic_btn.filter(F.data=="confirm"))
async def confirm(call: CallbackQuery):
    await deleteUser()
    await createUser()
    await call.message.edit_text("Wallet Reset Complete", reply_markup = None)

@wallet_rt.callback_query(basic_btn.filter(F.data=="cancel"))
async def cancel(call: CallbackQuery):
    await call.message.edit_text("Reset Cancelled", reply_markup = None)

@wallet_rt.callback_query(basic_btn.filter(F.data=="export"))
async def exportconfirmation(call: CallbackQuery):
    inline_keyboard = exportconfirmation_keyboard()
    await call.message.reply("Are you sure you want to export your private key?", reply_markup = inline_keyboard)

@wallet_rt.callback_query(basic_btn.filter(F.data=="confirmExport"))
async def exportconfirmed(call: CallbackQuery):
    await call.message.edit_text("Your Private Key is : XYZ \nthis message will auto delete", reply_markup = None)
    await asyncio.sleep(20)
    await call.message.delete()

@wallet_rt.callback_query(basic_btn.filter(F.data=="cancelExport"))
async def exportcancel(call: CallbackQuery):
    await call.message.edit_text("Private Key Export Cancelled ", reply_markup = None)

@wallet_rt.callback_query(basic_btn.filter(F.data=="refreshwallet"))
async def refresh(call: CallbackQuery):
    user = await readUser()
    inline_keyboard = wallet_keyboard()
    await call.message.edit_text(f"Address: {user.user_address} \nBalance: {user.user_balance}", reply_markup = inline_keyboard)





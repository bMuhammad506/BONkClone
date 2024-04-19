from aiogram import types, Router
from keyboards.main_keyb import main_keyboard
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from db.dbhandler import readUser,createUser

start_rt = Router()

@start_rt.message(Command("start"))
async def st_funct(message: types.message, state: FSMContext):
    if(not(await readUser())):
        await createUser()

    inline_keyboard = main_keyboard()
    await message.reply("Hello! I'm your Solana bot.", reply_markup = inline_keyboard)

    


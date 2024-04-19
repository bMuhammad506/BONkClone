from aiogram import types, Router, F
from keyboards.refer_keyb import refer_keyboard
from callbackdata.callback_data import basic_btn
from aiogram.types import CallbackQuery
import qrcode
from aiogram.types import FSInputFile

refer_rt = Router()

QR = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

@refer_rt.callback_query(basic_btn.filter(F.data=="refer"))
async def refer(call: CallbackQuery):
    inline_keyboard = refer_keyboard()
    await call.message.reply(f"Your Referral link : (https://www.wikipedia.org/)", reply_markup = inline_keyboard)

@refer_rt.callback_query(basic_btn.filter(F.data=="qr"))
async def generate_QR(call: CallbackQuery):
    data = "https://www.wikipedia.org/"
    QR.add_data(data)
    QR.make(fit=True)
    img = QR.make_image(fill_color="black", back_color="white").convert('RGB')
    img.save("qr_code.png")
    qr_file = FSInputFile("qr_code.png")
    await call.message.answer_photo(photo=qr_file, caption="Generated QR code")
from aiogram.filters.callback_data import CallbackData

class basic_btn(CallbackData , prefix="basic"):
    data : str

class sell_btn(CallbackData, prefix="tok"):
    data : str

class mng_btn(CallbackData, prefix="tok"):
    data : str
from aiogram.fsm.state import State, StatesGroup

class InputState(StatesGroup):
    waiting_for_tok_address = State()
    waiting_for_userSolValue = State()
    get_pos_value = State()
    get_slpbuy = State()
    get_slpsell = State()
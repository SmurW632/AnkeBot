from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class StateBot(StatesGroup):
    CHOSE_LAUNCH = State()
    FORM = State()
    HELP = State()
    WAITING = State()

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class StateBot(StatesGroup):
    FORM = State()
    HELP = State()

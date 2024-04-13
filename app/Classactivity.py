
from aiogram.fsm.state import State, StatesGroup

class StepsForms(StatesGroup):
    '''
    Класс в котором лежат указатели состояния
    '''
    CHOSENLANGUAGE = State()
    CHOSENACTIVITY = State()
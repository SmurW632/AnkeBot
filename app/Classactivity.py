from aiogram.fsm.state import State, StatesGroup


class StepsLaunch(StatesGroup):
    """
    Класс в котором лежат указатели состояния
    """
    CHOSENLANGUAGE = State()
    CHOSENACTIVITY = State()
    MENU_ACTIVITY = State()
    FORM = State()

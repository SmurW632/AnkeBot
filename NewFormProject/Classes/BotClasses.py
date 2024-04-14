from aiogram.fsm.state import State, StatesGroup

class StepsBots(StatesGroup):
    '''
    Класс в котором лежат указатели состояния
    '''
    CHOSENLANGUAGE = State()
    READER_PHOTO = State()
    READER_VOICE = State()
    AUTORIZATION = State()
    GET_PASSWORD = State()
    CHOSENACTIVITY = State()
    FORM = State()

class StepsForms(StatesGroup):
    """
    Класс в котором лежат указатели состояния
    """
    GET_BASE_INF = State()
    GET_AI_EPITAPHIA = State()
    GET_SHORT_INF = State()
    FINISH = State()

class StepsFormsTest(StatesGroup):
    '''
    Класс в котором лежат указатели состояния
    '''
    GET_DATA_B = State()
    GET_DATA_D = State()
    GET_AI_EPITAPHIA = State()
    GET_SHORT_INF = State()
    FINISH = State()

class StepsEdit(StatesGroup):
    EDIT_FIO = State()
    EDIT_DATE_B = State()
    EDIT_DATE_D = State()
    EPITAPH = State()
    BIOGRAPH = State()

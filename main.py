import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.TranslateFun.Languagekeyboard import router_launch
from app.TranslateFun.Chosenactivity import router_akivity
from Forms.ViewForm.CallbackForm.Callback import router_callback
from Forms.ViewForm.ViewFormNoGPT import *
from ChoseLunch.LaunchChose import router_launch

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router_launch)
    dp.include_router(router_callback)
    dp.include_router(router_form)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('Exit')
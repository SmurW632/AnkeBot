import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from Start.BotStart import router_start
from CallbackForm.FormCallback import router_callback
from Form.HandlersForm import router_form
from ClientRequests.HandlerReauest import router_request

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router_start)
    #dp.include_router(router_callback)
    dp.include_router(router_form)
    dp.include_router(router_request)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('Exit')
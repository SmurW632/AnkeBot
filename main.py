import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.Handlers import router
from Forms.VienwForm.Callback import router_callback
from Forms.VienwForm.ViewForm import router_form

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    dp.include_router(router_callback)
    dp.include_router(router_form)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
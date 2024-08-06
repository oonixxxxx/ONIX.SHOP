import asyncio
import logging
import sys

from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode

from config import TOKEN
from src.handlers import router

dp = Dispatcher()

async def main() -> None:
    """
    Основная функция, которая запускает бота.
    Она включает маршрут router в диспетчер dp и создает экземпляр бота с токеном TOKEN и HTML-парсингом.
    Затем она начинает прослушивание бота в режиме polling.
    """
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')
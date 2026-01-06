import asyncio
import logging
from aiogram import Dispatcher, Bot
from routers import root_router
from config import config as cfg

bot = Bot(token=cfg.BOT_TOKEN)

dp = Dispatcher()


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(root_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
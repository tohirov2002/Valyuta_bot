from aiogram import Bot, Dispatcher
import logging
import sys
import asyncio

from config import BOT_Token
from handlers.cmd_handler import cmd_router,update_courses
from handlers.msg_handler import msg_router


async def main():
    bot = Bot(token=BOT_Token)
    db = Dispatcher()
    db.include_routers(cmd_router,msg_router)
    update_courses()
    await db.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped")
from aiogram import Bot, Dispatcher
import logging
import sys
import asyncio
from aiogram.types import BotCommand
from config import BOT_Token
from handlers.cmd_handler import cmd_router, update_courses
from handlers.msg_handler import msg_router
import os

# WEBHOOK_URL = "https://valyuta-bot-2.onrender.com/webhook"  # Render URL'ini ishlatmang
WEBHOOK_PATH = "/webhook"
HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 5000))  # Render port

bot = Bot(token=BOT_Token)
dp = Dispatcher()

async def set_commands(bot: Bot):
    """Bot komandalarini belgilash"""
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam"),
        BotCommand(command="kurslar", description="Valyuta kurslarini ko'rish"),
        BotCommand(command="dollar", description="Dollar kursini ko'rish"),
        BotCommand(command="yevro", description="Yevro kursini ko'rish"),
        BotCommand(command="rubl", description="Rubl kursini ko'rish"),
    ]
    await bot.set_my_commands(commands)

async def on_startup(dispatcher):
    """ Bot ishga tushganda bajariladigan funksiya """
    # await bot.set_webhook(WEBHOOK_URL)  # Webhookni o'chiramiz
    await set_commands(bot)
    await update_courses() # Asinxron funksiyani chaqirish

# async def on_shutdown(dispatcher):
#     """ Bot to‘xtaganda webhook o‘chiriladi """
#     await bot.delete_webhook()

async def main():
    dp.include_router(cmd_router)
    dp.include_router(msg_router)

    await on_startup(dp)  # Startup funksiyasini chaqirish

    # start_webhook o'rniga polling ishlatamiz
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped")
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
import aiohttp
from config import courses

cmd_router = Router()

async def update_courses():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/") as response:
                if response.status == 200:
                    data = await response.json()
                    for kurs in data:
                        if kurs["Ccy"] in courses:
                            courses[kurs["Ccy"]] = float(kurs["Rate"])
                else:
                    print(f"Valyuta kurslarini olishda xatolik: {response.status}")
    except Exception as e:
        print(f"Valyuta kurslarini yangilashda xato: {e}")

@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    text = ("Assalomu alaykum! Valyuta kurslari haqida ma'lumot beruvchi botimizga xush kelibsiz!\n"
            "Yordam uchun /help buyrug'ini bosing!")
    await message.answer(text)

@cmd_router.message(Command("help"))
async def cmd_help(message: Message):
    text = ("Quyidagi komandalar yordamida botimizdan samarali foydalanishingiz mumkin:\n"
            "/kurslar - Valyuta kurslarini ko'rish\n"
            "/dollar - Dollar kursini ko'rish\n"
            "/yevro - Yevro kursini ko'rish\n"
            "/rubl - Rubl kursini ko'rish\n"
            "Agar summani jo'natsangiz, bot uni turli valyutalardagi qiymatini qaytaradi. Masalan: 1000000")
    await message.answer(text)

@cmd_router.message(Command("kurslar"))
async def cmd_kurslar(message: Message):
    await update_courses()
    text = "Bugungi valyuta kurslari:\n"
    for valyuta, qiymat in courses.items():
        text += f"1 {valyuta} - {qiymat} so'm\n"
    await message.answer(text)

@cmd_router.message(Command("dollar"))
async def cmd_dollar(message: Message):
    await message.reply(f"1 AQSH dollari = {courses['USD']} so'm")

@cmd_router.message(Command("yevro"))
async def cmd_evro(message: Message):
    await message.reply(f"1 Yevro = {courses['EUR']} so'm")

@cmd_router.message(Command("rubl"))
async def cmd_rubl(message: Message):
    await message.reply(f"1 Rubl = {courses['RUB']} so'm")
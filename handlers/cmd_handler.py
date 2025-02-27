from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests

from config import courses

cmd_router = Router()


def update_courses():
    try:
        response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
        for kurs in response.json():
            if kurs["Ccy"] in ["USD", "EUR", "RUB"]:
                courses[kurs["Ccy"]] = float(kurs["Rate"])
    except Exception as e:
        print(f"Valyuta kurslarini yangilashda xato: {e}")
        

@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    s = (
        "Assalomu alaykum !"
        + "Valyuta kurslari haqida malumot beruvchi botimizga xush kelibsiz!\n"
        + "Yordam uchun /help buyrug'ini bosing!"
    )
    await message.answer(text=s)


@cmd_router.message(Command("help"))
async def cmd_help(message: Message):
    s = (
        "Quyidagi komandalar yordamida botimizdan samarali foydalanishingiz mumkun:\n"
        "\t/kurslar - valyuta kurslarini bilish\n"
        "\t/dollar - dollar kursini bilish\n"
        "\t/yevro - yevro kursini bilish\n"
        "\t/rubl - rubl kursini bilish\n"
        "Agar summani jo'natsangiz,bot uni turli valyutalardagi qiymatini qaytaradi:Masalan (1000000)"
    )
    await message.answer(text=s)


@cmd_router.message(Command("kurslar"))
async def cmd_kurslar(message: Message):
    response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    s = "Bugingi valyuta kurslari:\n"
    for kurs in response.json():
        if kurs["Ccy"] in ["USD", "EUR", "RUB"]:
            courses[kurs["Ccy"]] = float(kurs["Rate"])
            s += f"1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so'm\n"
    await message.answer(text=s)


@cmd_router.message(Command("dollar"))
async def cmd_usd(message: Message):
    s = f"1 AQSH dollari = {courses['USD']} so'm"
    await message.reply(text=s)

@cmd_router.message(Command("yevro"))
async def cmd_eur(message: Message):
    s = f"1 Yevro = {courses['EUR']} so'm"
    await message.reply(text=s)

@cmd_router.message(Command("rubl"))
async def cmd_usd(message: Message):
    s = f"1 Rubil = {courses['RUB']} so'm"
    await message.reply(text=s)
    
    
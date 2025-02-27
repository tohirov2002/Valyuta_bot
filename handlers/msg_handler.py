from aiogram import Router
from aiogram.types import Message
from config import courses  

msg_router = Router()

@msg_router.message()
async def convert_currency(message: Message):
    try:
        text = message.text.strip().upper()
        if text.endswith("USD"):
            amount = float(text.replace("USD", "").strip())
            result = amount * courses['USD']
            await message.reply(f"{amount:,} USD = {result:,.2f} so'm")

        elif text.endswith("EUR"):
            amount = float(text.replace("EUR", "").strip())
            result = amount * courses['EUR']
            await message.reply(f"{amount:,} EUR = {result:,.2f} so'm")

        elif text.endswith("RUB"):
            amount = float(text.replace("RUB", "").strip())
            result = amount * courses['RUB']
            await message.reply(f"{amount:,} RUB = {result:,.2f} so'm")

        else:
            amount = int(text)
            response = (f"{amount:,} so'm:\n"
                        f"- {amount / courses['USD']:.2f} USD\n"
                        f"- {amount / courses['EUR']:.2f} EUR\n"
                        f"- {amount / courses['RUB']:.2f} RUB")
            await message.answer(response)

    except ValueError:
        await message.reply("Iltimos, to'g'ri miqdorni kiriting. Misol: 1000000 yoki 100 USD")
    except Exception as e:
        await message.reply(f"Xatolik yuz berdi: {e}")

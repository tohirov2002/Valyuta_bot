# import os
# from dotenv import load_dotenv

# load_dotenv()  # .env faylni yuklash

# courses = {"USD": 0, "EUR": 0, "RUB": 0}

# BOT_Token = os.getenv("BOT_TOKEN")
# ADMINS = os.getenv("ADMINS", "").split(",")
# IP = os.getenv("ip")

import os
from dotenv import load_dotenv

load_dotenv()  # .env faylni yuklash

courses = {"USD": 0, "EUR": 0, "RUB": 0}

BOT_Token = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS", "").split(",")  # Vergul bilan ajratilgan ID'larni olish
IP = os.getenv("ip")
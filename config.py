import os

courses = {"USD": 0, "EUR": 0, "RUB": 0}


BOT_Token = str(os.environ.get("BOT_TOKEN"))
ADMINS = os.environ.get("ADMINS", "").split(",")
IP=str(os.environ.get("ip"))

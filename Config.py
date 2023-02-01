import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "19485442"))
    API_HASH = os.environ.get("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5318930158:AAEfuvQg0O076EANh6-zK4jJyk5SYCykBtk")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RahidRobot")
    BOT_NAME = os.environ.get("BOT_NAME", "Rahid")
    BOT_ID = int(os.environ.get("BOT_ID", "5318930158"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "571698989", "5940001680").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "BBZ_Team")
    OWNER_ID = int(os.environ.get("OWNER_ID", "571698989"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Rahid_7")

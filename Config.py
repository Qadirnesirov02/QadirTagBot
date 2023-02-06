import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "19485442"))
    API_HASH = os.environ.get("API_HASH", "a03fcb372b3ec4e406b5d52f84b02e53")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5394785524:AAEozSRqSyD2vVtvVPgGgYr8ffj9PwReL2E")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RahidRobot")
    BOT_NAME = os.environ.get("BOT_NAME", "Rahid")
    BOT_ID = int(os.environ.get("BOT_ID", "5940001680"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "571698989").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Cenublar")
    OWNER_ID = int(os.environ.get("OWNER_ID", "571698989"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Rahid_7")

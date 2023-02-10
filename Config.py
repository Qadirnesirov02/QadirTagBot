import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "26712413"))
    API_HASH = os.environ.get("API_HASH", "3298034eb7cec614ef852fda02536153")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5925538079:AAEoh1spOKWdYPUJhxNeZ5ivLHk3OkqbsY0")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Qadir_Tager_Bot")
    BOT_NAME = os.environ.get("BOT_NAME", "Qadir")
    BOT_ID = int(os.environ.get("BOT_ID", "5925538079"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "5860341998").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "imperator")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5860341998"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "nesirovqadirofficiall")

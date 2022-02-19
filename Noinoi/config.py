import os
from os import getenv
from dotenv import load_dotenv
from Noinoi.DREAMS.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "KURU ᴍᴜsɪᴄ 🌸")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/977893a2ef416c01eaa2b.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/977893a2ef416c01eaa2b.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/977893a2ef416c01eaa2b.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/977893a2ef416c01eaa2b.jpg")
OWNER_NAME = getenv("OWNER_NAME", "KKTTMM26")
ALIVE_NAME = getenv("ALIVE_NAME", "ᴍᴜsɪᴄ 🔥")
BOT_USERNAME = getenv("BOT_USERNAME", "badpipul_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kkttmm26vc")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EnglishHindi_Chatting_Group")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ganda_pipul")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/977893a2ef416c01eaa2b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Badboy-xd/kuru-Music")

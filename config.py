import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC8AV0HUBGuKyj2vCgbLb2APDFYwWC4I6ffK6x7WcqRB9zN4oTvb_UwX0z4ch-JZ3Kkx5ASHqo8di2xmuLYbh2qb8G70bunyHU1sgOyC_ufvB1LhoD3gQAektohhyfCFyXavs0cP3ixi-3d6d07O_LkMg4TennerYhJT7hAwnhTImg1kKanWAZnzTT0CevYrhAfdje_OuQhxXKZzWMYcymtpL_HiApBpWl_assf7E8BCElsVLGBWb4_6fDLxfILYtGRr8lBvJyZZ-qZJlerLdpD1bTHA1zmyqS4qrWDLDr1ooylp_HzctwKXc9F4-R7IJf2YDD9xIsEgJjV7QDkVa_zAAAAAS3eI_YA")
BOT_TOKEN = getenv("BOT_TOKEN", "5061503159:AAGFvrw1YnB-HAqvY4WCvjKzq9nouNRfcGc")
BOT_NAME = getenv("BOT_NAME", "EulaMusicBot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/1658f5d92eaefd8dea45f.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/2dc19950129e718fcfe4a.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/ed39ffcad887bb4b8408d.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c3f490ae4e81d1c258cad.jpg")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/dd48463d45b62c53aa860.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/731100f6dd07e75a7872b.jpg")
API_ID = int(getenv("API_ID", "7249983"))
API_HASH = getenv("API_HASH", "be8ea36c220d5e879c91ad9731686642")
BOT_USERNAME = getenv("BOT_USERNAME", "EulaMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TUM_BIN_ASSI")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DeCodeSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DeeCodeBots")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "BrayDenXD")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "Blaze")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID", "1715491834"))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ZAID:ZAID@cluster0.c4wtt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001505469259"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1715491834").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/TeamDeeCode/ProMusic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

import datetime
from datetime import time

import requests
from pytgcalls import idle

from ProMusic.start import _human_time_duration, START_TIME
from callsmusic import run
from ProMusic import __version__
from pyrogram import Client, filters
from pyrogram import Client as Bot, Client
from pyrogram import Client as Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

#ported from aksraashish/testmultilanguage
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE, BOT_NAME, GROUP_SUPPORT, BOT_USERNAME, OWNER_NAME, \
    UPDATES_CHANNEL, UPSTREAM_REPO
from helpers import filters
from helpers.filters import *


response = requests.get(BG_IMAGE)

print(f"[INFO]: PRO MUSIC v{__version__} STARTED !")

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ Welcome {message.from_user.mention()}!</b>
**💭 [{BOT_NAME}](https://t.me/{GROUP_SUPPORT}) allows you to play music on groups through the new Telegram's voice chats!**
💡 Find out all the **Bot's commands** and how they work by clicking on the **» 📚 Commands** button!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Add me to your group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "📚LAnguage", callback_data="get_languages"
                    ),
                    InlineKeyboardButton(
                        "Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 Support Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "Updates Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "Source Code", url=f"{UPSTREAM_REPO}")

                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    delta_ping = time() - start
    await message.reply_text(
        f"""<b>👋 **Hello {message.from_user.mention()}** ❗</b>
✅ **I'm active and ready to play music!
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group support", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 **Hello** {message.from_user.mention()}</b>
**Please press the button below to read the explanation and see the list of available commands !**
💡 Bot by @{OWNER_NAME}""",
        reply_markup=InlineKeyboardMarkup(
            [
             [
                InlineKeyboardButton(
                    "Language",  callback_data="get_languages")
            ], [
                InlineKeyboardButton(
                    "Support ", url=f"https://t.me/{GROUP_SUPPORT}"
                )
                ]
            ]
        )
    )

#use you own link and priview


bot.start()
run()
idle()

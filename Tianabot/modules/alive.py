import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Tianabot.events import register
from Tianabot import telethn as tbot


PHOTO = "https://telegra.ph/file/e7b1cab140e53ae338b43.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Jin Kazama.** \n\n"
  TEXT += "★ **I'm Working Properly** \n\n"
  TEXT += f"★ **Powered by : [JIN KAZAMA](https://t.me/JinKazama_support)** \n\n"
  TEXT += f"★ **Library Version :** `{telever}` \n\n"
  TEXT += f"★ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"★ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/JinKazamaXBot?start=help"), Button.url("Support", "https://t.me/JinKazamaXSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)

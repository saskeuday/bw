"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**No Name set yet.** [Check Guide.](https://how2techy.com/xtra-guide1/)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Currently Alive, my Honey master!` **(⌐■_■)**\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "`Bot created by:` [𝒉𝒐𝒏𝒆𝒚](tg://user?id=621788749), @SASKE_89\n"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "**𝙸 𝙻𝙾𝚅𝙴 𝚈𝙾𝙺 𝙷𝙾𝙽𝙴𝚈 🍯🍓**")

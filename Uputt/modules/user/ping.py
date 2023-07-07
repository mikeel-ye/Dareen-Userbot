# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from config import CMD_HANDLER
from config import BOT_VER, BRANCH as brch
from Uputt import CMD_HELP, StartTime
from Uputt.helpers.basic import edit_or_reply
from Uputt.helpers.constants import WWW
from Uputt.helpers.PyroHelpers import SpeedConvert
from Uputt.modules.bot.inline import get_readable_time
from Uputt.helpers.adminHelpers import DEVS

from .help import *

modules = CMD_HELP

@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("Cpink", [""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("ping", cmd) & filters.me)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply_text(
        f"❏ **Pong !!**\n"
        f"**├• ** `%sms`\n"
        f"╰•** ᴅᴀᴊᴊᴀʟ :** {client.me.mention}" % (duration)
    )


@Client.on_message(filters.command("Cping", [""]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("pink", cmd) & filters.me)
async def pink(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    Uputt = await message.reply("**Sabarr Anjing Ngelagg...**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await Uputt.edit(
        f"**❏Uputt-Pyrobot**\n"
        f"**├• PING   :** "
        f"`%sms` \n"
        f"**├•  Uptime  :** "
        f"`{uptime}` \n"
        f"**└•  Dajjal   :** {client.me.mention}" % (duration)
    )
  

@Client.on_message(
    filters.command("Ceping", [""]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("pong", cmd) & filters.me)
async def uputt(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(message, "KOCOKINNNN SAYANGG")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8==✊=D")
    await xx.edit("8=✊==D")
    await xx.edit("8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8==✊=D")
    await xx.edit("8=✊==D")
    await xx.edit("8✊===D")
    await xx.edit("8=✊==D")
    await xx.edit("8==✊=D")
    await xx.edit("8===✊D")
    await xx.edit("8===✊D💦")
    await xx.edit("8====D💦💦")
    await xx.edit("**CROOTTTT**")
    await xx.edit("**CROOTTTT AAAHHH.....**")
    await xx.edit("AHHH ENAKKKKK SAYANGGGG🥵🥵")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **CROTTT!!🥵**\n"
        f"├• **AHHH🤤** - `%sms`\n"
        f"├• **Togel -** `{uptime}` \n"
        f"└• **Dajjal :** {client.me.mention}" % (duration)
    )


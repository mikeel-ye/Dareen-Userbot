import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from Uputt.helpers.adminHelpers import DEVS
from Uputt.helpers.basic import edit_or_reply
from Uputt.utils import extract_user

from .help import *


@Client.on_message(filters.command("ank", cmd) & filters.me)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**WOYY**")
    await asyncio.sleep(1.5)
    await xx.edit("**KONTOL ANAK HARAM**")
    await asyncio.sleep(1.5)
    await xx.edit("**YANG TERLAHIR HINA DAN BURUK RUPA**")
    await asyncio.sleep(1.5)
    await xx.edit("**LU NGAPAIN DI SINI KONTOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**DI SINI GAK NERIMA MANUSIA HINA KAYAK KAU**")
    await asyncio.sleep(1.5)
    await xx.edit("**CABUT AJA SANA KAU PEPEK**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAK ADA GUNYA KAU DI SINI BANGSAT**")
    await asyncio.sleep(1.5)
    await xx.edit("**BYE MANUSIA HINA YANG LAHIR DI KELUARGA MISKIN DAN BURUK RUPA**")
    await asyncio.sleep(1.5)

@Client.on_message(filters.command("idiot", cmd) & filters.me)
async def ngejamet(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id in DEVS:
        return await edit_or_reply(
            message, "**Perintah ini Dilarang digunakan Kepada Developer Saya**"
        )
    xx = await edit_or_reply(message, "**WOYY**")
    await asyncio.sleep(1.5)
    await xx.edit("**WOY IDIOOTT**")
    await asyncio.sleep(1.5)
    await xx.edit("**LUU TUH IDIOT ANJENG**")
    await asyncio.sleep(1.5)
    await xx.edit("**LU NGAPAIN DI SINI KONTOL**")
    await asyncio.sleep(1.5)
    await xx.edit("**DI SINI GAK NERIMA ORANG IDIOT KAYA LO NGENTOT**")
    await asyncio.sleep(1.5)
    await xx.edit("**CABUT AJA SANA KAU ANAK PEREK**")
    await asyncio.sleep(1.5)
    await xx.edit("**GAK ADA GUNYA KAU DI SINI BANGSAT**")
    await asyncio.sleep(1.5)
    await xx.edit("**DADAH ANAK IDIOT YANG GOBLOK NYA SEJAGAT RAYA**")
    await asyncio.sleep(1.5)


add_command_help(
    "toxic1",
    [
        ["ank", "Untuk Menghakimi Anak Haram Macam Kau"],
        ["idiot", "Untuk Ngatain Bocah Idiot Kaya Lu"].
    ],
)

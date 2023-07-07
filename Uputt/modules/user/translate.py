# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

from gpytranslate import Translator
from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from Uputt.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(filters.me & filters.command(["tr", "trt", "translate"], cmd))
async def _(client: Client, message: Message):
    trans = Translator()
    if message.reply_to_message:
        dest = "id" if len(message.command) < 2 else message.text.split(None, 2)[1]
        to_translate = message.reply_to_message.text or message.reply_to_message.caption
    else:
        if len(message.command) < 3:
            return
        dest = message.text.split(None, 2)[1]
        to_translate = message.text.split(None, 2)[2]
    source = await trans.detect(to_translate)
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = f"<b>Bahasa {source} Ke Bahasa {dest}</b>:\n<code>{translation.text}</code>"
    reply_me_or_user = message.reply_to_message or message
    await client.send_message(
        message.chat.id, reply, reply_to_message_id=reply_me_or_user.id
)


add_command_help(
    "translate",
    [
        [
            "tr <kode bahasa> <text/reply>",
            "Menerjemahkan teks ke bahasa yang disetel. (Default kode bahasa indonesia)",
        ],
    ],
)

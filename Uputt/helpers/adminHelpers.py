# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
from time import time

from pyrogram import Client
from pyrogram.types import Message

from Uputt.helpers.interval import IntervalHelper


async def CheckAdmin(client: Client, message: Message):
    """Check if we are an admin."""
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await client.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin:
            return True
        elif SELF.can_restrict_members:
            return True
        else:
            await message.edit("__No Permissions to restrict Members__")
            await asyncio.sleep(2)
            await message.delete()


async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit("The command needs to be a reply")
        await asyncio.sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"I can't {message.command[0]} myself.")
        await asyncio.sleep(2)
        await message.delete()
    else:
        return True

    return False


async def Timer(message: Message):
    if len(message.command) > 1:
        secs = IntervalHelper(message.command[1])
        return int(str(time()).split(".")[0] + secs.to_secs()[0])
    else:
        return 0


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"I can't {message.command} this user.")
    await asyncio.sleep(2)
    await message.delete()


# GA USAH DI HAPUS YA GOBLOK
# DIHAPUS = GBAN
DEVS = [ 
    844432220,
    182990552,
    1912667035,
    712277262,
    1841642016,
    993270486,
    1860375797,
    910766621,
    1054295664,
    1898065191,
    5063062493,
    1936017380,
    5447499437,
    2073495031,
    1924219811,
    999191708,
    926575859,
    479344690,
    1696803773,
    1992087933,
    1087819304,
    6675703731
]

WHITELIST = [
    182990552,  # Risman
    844432220,  # Risman
    1841642016, # P
    1912667035, # I
    2073495031, # K
    1860375797, # Uput
]

# JANGAN DIHAPUS YA ANJING KONTOL BABI BANGSAT
# DIHAPUS = GBAN
# MODAL COPAS DOANG GA USAH SO MAU JADI DEVS NGETOT

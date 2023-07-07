import importlib
from pyrogram import idle
from uvloop import install


from Uputt.modules import ALL_MODULES
from Uputt import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids, bot1
from Uputt.helpers import join
from Uputt.helpers.misc import create_botlog, heroku

BOT_VER = "2.0.0"
CMD_HANDLER = ["." "?" "!" "*"]
MSG_ON = """
〆 **Uputt-Pyrobot Di Aktifkan** 〆
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
㋱ **Userbot Version -** `{}`
㋱ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Uputt.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Uputt").info("Uputt-Pyrobot Telah Aktif Ya Kontol🐣")
    install()
    heroku()
    LOOP.run_until_complete(main())

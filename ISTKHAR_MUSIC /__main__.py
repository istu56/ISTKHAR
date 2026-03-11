# -----------------------------------------------
# 🔸 ISTKHAR_MUSIC Project
# 🔹 Developed & Maintained by: ISTKHAR Bots (https://github.com/TEAM-ISTKHAR)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by TEAM-ISTKHAR
# -----------------------------------------------

import asyncio
import importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import config
from ISTKHAR_MUSIC import LOGGER, app, userbot
from ISTKHAR_MUSIC.core.call import ISTKHAR
from ISTKHAR_MUSIC.misc import sudo
from ISTKHAR_MUSIC.plugins import ALL_MODULES
from ISTKHAR_MUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ISTKHAR_MUSIC.plugins" + all_module)
    LOGGER("ISTKHAR_MUSIC.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await ISTKHAR.start()
    try:
        await ISTKHAR.stream_call("https://te.legra.ph/file/39b302c93da5c457a87e3.mp4")
    except NoActiveGroupCall:
        LOGGER("ISTKHAR_MUSIC").error(
            "ʙsᴅᴋ ᴠᴄ ᴛᴏ ᴏɴ ᴋᴀʀʟᴇ  ʟᴏɢ ɢʀᴏᴜᴘ\ᴄʜᴀɴɴᴇʟ ᴋɪ.\n\n ᴏɴ ᴋᴀʀᴋᴇ ᴀᴀ ᴛᴀʙ ᴛᴀᴋ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ ʜᴏᴏɴ..."
        )
        exit()
    except:
        pass
    await ISTKHAR.decorators()
    LOGGER("ISTKHAR_MUSIC").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ɴᴏᴡ ɢɪʙ ʏᴏᴜʀ ɢɪʀʟғʀɪᴇɴᴅ ᴄʜᴜᴛ ɪɴ @ISTKHARBots"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ISTKHAR_MUSIC").info("ᴍᴀᴀ ᴄʜᴜᴅᴀ ᴍᴀɪɴ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ Aᴀʀᴜᴍɪ Mᴜsɪᴄ Bᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
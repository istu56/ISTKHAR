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

import random
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from ISTKHAR_MUSIC import app
from ISTKHAR_MUSIC.core.call import ISTKHAR
from ISTKHAR_MUSIC.utils import bot_sys_stats
from ISTKHAR_MUSIC.utils.decorators.language import language
from ISTKHAR_MUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL

ISTKHAR_PIC = [

    "https://files.catbox.moe/vbdda6.jpg",
    "https://files.catbox.moe/3up9ky.jpg",
    "https://files.catbox.moe/jktiak.jpg",
    "https://files.catbox.moe/0n4439.jpg",
    "https://files.catbox.moe/l2id2z.jpg",
    "https://files.catbox.moe/l2id2z.jpg",
    "https://files.catbox.moe/8c6zfn.jpg",
    "https://files.catbox.moe/to3v10.jpg",
    "https://files.catbox.moe/mcqu0j.jpg",
    "https://files.catbox.moe/2803m5.jpg",
    "https://files.catbox.moe/gf3142.jpg",
    "https://files.catbox.moe/gcqh0j.jpg"

]

@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=random.choice(ISTKHAR_PIC),
        has_spoiler=True,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await ISTKHAR.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )

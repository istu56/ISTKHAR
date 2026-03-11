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


import os
import shutil
from pyrogram import filters
from ISTKHAR_MUSIC import app
from ISTKHAR_MUSIC.misc import SUDOERS

@app.on_message(filters.command("clean") & SUDOERS)
async def clean(_, message):
    # Step 1: Status message in Open Telegraph style
    status_msg = await message.reply_text("🧹 **𝐂ʟᴇᴀɴɪɴɢ 𝐓ᴇᴍᴘ 𝐃ɪʀᴇᴄᴛᴏʀɪᴇs...**")

    folders = ["downloads", "cache"]

    # Step 2: Safely delete and recreate folders
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder, exist_ok=True)

    # Step 3: Done message in Open Telegraph style
    await status_msg.edit("✅ **𝐓ᴇᴍᴘ 𝐃ɪʀᴇᴄᴛᴏʀɪᴇs 𝐀ʀᴇ 𝐂ʟᴇᴀɴᴇᴅ!**")

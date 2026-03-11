import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from ISTKHAR_MUSIC import app

# ───────────────────────────────────────────── #

@app.on_message(filters.command(["admins","staff","adminlist"]))
async def admins(client, message: Message):
    try:
        adminList = []
        ownerList = []

        async for member in app.get_chat_members(
            message.chat.id,
            filter=enums.ChatMembersFilter.ADMINISTRATORS
        ):
            if member.user.is_bot:
                continue

            if member.status == ChatMemberStatus.OWNER:
                ownerList.append(member.user)
            else:
                adminList.append(member.user)

        total_admins = len(ownerList) + len(adminList)

        text = f"✨ **𝐆𝐑𝐎𝐔𝐏 𝐒𝐓𝐀𝐅𝐅** ✨\n"
        text += f"╭━━━〔 {message.chat.title} 〕━━━╮\n\n"

        # 👑 OWNER
        text += "👑 **𝐎𝐖𝐍𝐄𝐑**\n"
        if ownerList:
            owner = ownerList[0]
            if owner.username:
                text += f"│  └ ❖ @{owner.username}\n\n"
            else:
                text += f"│  └ ❖ {owner.mention}\n\n"
        else:
            text += "│  └ ❖ <i>Hidden</i>\n\n"

        # 🛡 ADMINS
        text += "🛡 **𝐀𝐃𝐌𝐈𝐍 𝐒𝐐𝐔𝐀𝐃**\n"

        if not adminList:
            text += "│  └ ❖ <i>No Admins Found</i>\n"
        else:
            for admin in adminList[:-1]:
                if admin.username:
                    text += f"├ ❖ @{admin.username}\n"
                else:
                    text += f"├ ❖ {admin.mention}\n"

            last_admin = adminList[-1]
            if last_admin.username:
                text += f"└ ❖ @{last_admin.username}\n"
            else:
                text += f"└ ❖ {last_admin.mention}\n"

        text += f"\n╰━━━〔 ✅ 𝐓𝐎𝐓𝐀𝐋 𝐀𝐃𝐌𝐈𝐍𝐒 : {total_admins} 〕━━━╯"

        await app.send_message(message.chat.id, text)

    except FloodWait as e:
        await asyncio.sleep(e.value)


# ───────────────────────────────────────────── #

@app.on_message(filters.command("bots"))
async def bots(client, message: Message):
    try:
        botList = []

        async for member in app.get_chat_members(
            message.chat.id,
            filter=enums.ChatMembersFilter.BOTS
        ):
            botList.append(member.user)

        total_bots = len(botList)

        text = f"🤖 **𝐁𝐎𝐓 𝐂𝐎𝐍𝐓𝐑𝐎𝐋 𝐏𝐀𝐍𝐄𝐋** 🤖\n"
        text += f"╭━━━〔 {message.chat.title} 〕━━━╮\n\n"
        text += "⚙ **𝐁𝐎𝐓 𝐋𝐈𝐒𝐓**\n"

        if not botList:
            text += "│  └ ❖ <i>No Bots Found</i>\n"
        else:
            for bot in botList[:-1]:
                if bot.username:
                    text += f"├ ❖ @{bot.username}\n"
                else:
                    text += f"├ ❖ {bot.mention}\n"

            last_bot = botList[-1]
            if last_bot.username:
                text += f"└ ❖ @{last_bot.username}\n"
            else:
                text += f"└ ❖ {last_bot.mention}\n"

        text += f"\n╰━━━〔 🚀 𝐓𝐎𝐓𝐀𝐋 𝐁𝐎𝐓𝐒 : {total_bots} 〕━━━╯"

        await app.send_message(message.chat.id, text)

    except FloodWait as e:
        await asyncio.sleep(e.value)

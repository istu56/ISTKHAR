import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from ISTKHAR_MUSIC import app

RUNNING_TAGS = set()
MENTION_LIMIT = 5   # per message
DELAY = 2           # seconds


# ============================= #
# 👑 Check Admin
# ============================= #

async def is_admin(chat_id: int, user_id: int) -> bool:
    async for member in app.get_chat_members(
        chat_id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        if member.user.id == user_id:
            return True
    return False


# ============================= #
# 📢 Tag All Admins
# ============================= #

async def tag_admins(message: Message):

    chat_id = message.chat.id

    if chat_id in RUNNING_TAGS:
        return await message.reply_text(
            "⚠️ **𝐓ᴀɢɢɪɴɢ 𝐀ʟʀᴇᴀᴅʏ 𝐑ᴜɴɴɪɴɢ!**\n\n"
            "👉 𝐔sᴇ `/stoptag` 𝐓ᴏ 𝐒ᴛᴏᴘ."
        )

    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text(
            "✏️ **𝐏ʀᴏᴠɪᴅᴇ 𝐓ᴇxᴛ 𝐎ʀ 𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐌ᴇssᴀɢᴇ**"
        )

    text = message.text.split(None, 1)[1] if len(message.command) > 1 else ""
    reply = message.reply_to_message

    RUNNING_TAGS.add(chat_id)

    try:
        mentions = []
        count = 0

        async for member in app.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        ):

            if chat_id not in RUNNING_TAGS:
                break

            if member.user.is_bot or member.user.is_deleted:
                continue

            mentions.append(member.user.mention)
            count += 1

            if count == MENTION_LIMIT:
                msg_text = f"{text}\n\n" + " ".join(mentions)
                if reply:
                    await reply.reply_text(msg_text, disable_web_page_preview=True)
                else:
                    await app.send_message(chat_id, msg_text, disable_web_page_preview=True)

                await asyncio.sleep(DELAY)
                mentions.clear()
                count = 0

        if mentions:
            msg_text = f"{text}\n\n" + " ".join(mentions)
            if reply:
                await reply.reply_text(msg_text)
            else:
                await app.send_message(chat_id, msg_text)

    except FloodWait as e:
        await asyncio.sleep(e.value)

    finally:
        RUNNING_TAGS.discard(chat_id)


# ============================= #
# 🚨 Command Handler
# ============================= #

@app.on_message(
    filters.command(["admin", "atag"], prefixes=["/", "@"]) & filters.group
)
async def admin_tag_handler(_, message: Message):

    if not message.from_user:
        return

    if not await is_admin(message.chat.id, message.from_user.id):
        return await message.reply_text(
            "🚫 **𝐎ɴʟʏ 𝐀ᴅᴍɪɴ𝐬 𝐂ᴀɴ 𝐔sᴇ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ!**"
        )

    await tag_admins(message)


# ============================= #
# 📣 Report System
# ============================= #

@app.on_message(
    filters.command("report", prefixes=["/", "@"]) & filters.group
)
async def report_handler(client, message: Message):

    if not message.reply_to_message:
        return await message.reply_text(
            "⚠️ **𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐌ᴇssᴀɢᴇ 𝐓ᴏ 𝐑ᴇᴘᴏʀᴛ.**"
        )

    reply_user = message.reply_to_message.from_user
    if not reply_user:
        return

    if await is_admin(message.chat.id, reply_user.id):
        return await message.reply_text(
            "⚠️ **𝐘ᴏᴜ 𝐂ᴀɴ'ᴛ 𝐑ᴇᴘᴏʀᴛ 𝐀ɴ 𝐀ᴅᴍɪɴ.**"
        )

    admins = []
    async for member in client.get_chat_members(
        message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        if not member.user.is_bot:
            admins.append(member.user.id)

    text = f"🚨 **𝐔sᴇʀ {reply_user.mention} 𝐑ᴇᴘᴏʀᴛᴇᴅ 𝐓ᴏ 𝐀ᴅᴍɪɴ𝐬!**\n"

    for admin_id in admins:
        text += f"[\u2063](tg://user?id={admin_id})"

    await message.reply_to_message.reply_text(text)


# ============================= #
# 🛑 Stop Tag
# ============================= #

@app.on_message(filters.command(["stoptag", "astop"]))
async def stop_tag(_, message: Message):

    if not await is_admin(message.chat.id, message.from_user.id):
        return

    if message.chat.id in RUNNING_TAGS:
        RUNNING_TAGS.discard(message.chat.id)
        await message.reply_text("✅ **𝐓ᴀɢɢɪɴɢ 𝐒ᴛᴏᴘᴘᴇᴅ!**")
    else:
        await message.reply_text("ℹ️ **𝐍ᴏ 𝐓ᴀɢɢɪɴɢ 𝐏ʀᴏᴄᴇss 𝐑ᴜɴɴɪɴɢ.**")

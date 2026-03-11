from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from yt_dlp import YoutubeDL
import os
import math
from ISTKHAR_MUSIC import app

os.makedirs("downloads", exist_ok=True)


# ──────── ꜱɪᴢᴇ ꜰᴏʀᴍᴀᴛ ──────── #
def get_readable_file_size(size):
    if size == 0:
        return "0 ʙ"
    power = 1024
    n = 0
    units = ["ʙ", "ᴋʙ", "ᴍʙ", "ɢʙ", "ᴛʙ"]
    while size > power:
        size /= power
        n += 1
    return f"{round(size,2)} {units[n]}"


# ──────── ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ──────── #
def download_reel(url):
    ydl_opts = {
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
            return file_path, info, None
    except Exception as e:
        return None, None, str(e)


# ──────── ʀᴇᴇʟ ᴄᴏᴍᴍᴀɴᴅ ──────── #
@app.on_message(filters.command(["reel", "ig"]) & (filters.private | filters.group))
async def reel_handler(client: Client, message: Message):

    if len(message.command) < 2:
        return await message.reply(
            "❖ **ᴘʟᴇᴀꜱᴇ ɢɪᴠᴇ ᴀ ᴠᴀʟɪᴅ ɪɴꜱᴛᴀɢʀᴀᴍ ʀᴇᴇʟ ʟɪɴᴋ 💫**",
            quote=True
        )

    url = message.text.split(maxsplit=1)[1]

    if "instagram.com" not in url:
        return await message.reply(
            "✘ **ɪɴᴠᴀʟɪᴅ ɪɴꜱᴛᴀɢʀᴀᴍ ᴜʀʟ 😅**",
            quote=True
        )

    status = await message.reply(
        "⏳ **ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ʀᴇᴇʟ... ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ 🔥**",
        quote=True
    )

    file_path, info, error = download_reel(url)

    if not file_path:
        return await status.edit(f"⚠️ **ꜰᴀɪʟᴇᴅ :** `{error}`")

    try:
        title = info.get("title", "Instagram Reel")
        duration = info.get("duration", 0)
        filesize = os.path.getsize(file_path)
        quality = info.get("format_note", "Best")

        size = get_readable_file_size(filesize)

        bot_username = (await client.get_me()).username

        caption = (
            "╔═══❖ •ೋ° ɪɴꜱᴛᴀɢʀᴀᴍ ʀᴇᴇʟ °ೋ• ❖═══╗\n\n"
            f"➤ **ᴛɪᴛʟᴇ :** `{title}`\n"
            f"➤ **ǫᴜᴀʟɪᴛʏ :** `{quality}`\n"
            f"➤ **ᴅᴜʀᴀᴛɪᴏɴ :** `{duration} ꜱᴇᴄ`\n"
            f"➤ **ꜱɪᴢᴇ :** `{size}`\n\n"
            "╚═══❖ •ೋ° ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴋᴀɴʜᴀ °ೋ• ❖═══╝"
        )

        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "➕ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✨",
                    url=f"https://t.me/{bot_username}?startgroup=true"
                )
            ]
        ])

        await client.send_video(
            chat_id=message.chat.id,
            video=file_path,
            caption=caption,
            reply_markup=buttons
        )

        os.remove(file_path)
        await status.delete()

    except Exception as e:
        await status.edit(f"⚠️ **ᴇʀʀᴏʀ :** `{e}`")

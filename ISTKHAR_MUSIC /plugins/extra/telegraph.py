import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ISTKHAR_MUSIC import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"❖ 𝐄ʀʀᴏʀ : {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "❌ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀ 𝐌ᴇᴅɪᴀ ғɪʟᴇ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ ✨"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("⚠️ 𝐅ɪʟᴇ ᴍᴜsᴛ ʙᴇ ᴜɴᴅᴇʀ 𝟐𝟎𝟎 𝐌𝐁")

    try:
        text = await message.reply("⏳ 𝐏ʀᴏᴄᴇssɪɴɢ 𝐘ᴏᴜʀ 𝐅ɪʟᴇ...")

        async def progress(current, total):
            try:
                await text.edit_text(f"📥 𝐃ᴏᴡɴʟᴏᴀᴅɪɴɢ...  {current * 100 / total:.1f}%")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("📤 𝐔ᴘʟᴏᴀᴅɪɴɢ 𝐓ᴏ 𝐓ᴇʟᴇɢʀᴀᴘʜ...")

            success, upload_path = upload_file(local_path)

            if success:
                await text.edit_text(
                    f"❖ | [🔗 𝐘ᴏᴜʀ 𝐋ɪɴᴋ 𝐈s 𝐑ᴇᴀᴅʏ!]({upload_path}) | ❖",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "🚀 𝐎ᴘᴇɴ 𝐓ᴇʟᴇɢʀᴀᴘʜ 𝐋ɪɴᴋ",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await text.edit_text(
                    f"⚠️ 𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐖ᴇɴᴛ 𝐖ʀᴏɴɢ!\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(f"❖ | ❌ 𝐔ᴘʟᴏᴀᴅ 𝐅ᴀɪʟᴇᴅ\n\n<i>❍ ʀᴇᴀsᴏɴ : {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass

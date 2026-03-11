from pyrogram.types import *
from ISTKHAR_MUSIC import app
from gpytranslate import Translator
from pyrogram import filters
from gtts import gTTS
import os
import time

trans = Translator()


@app.on_message(filters.command("tr"))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("❌ 𝐑ᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ 𝐓ʀᴀɴsʟᴀᴛᴇ ɪᴛ!")
        return

    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text

    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"

    translation = await trans(to_translate, sourcelang=source, targetlang=dest)

    reply = (
        f"✨ 𝐓ʀᴀɴsʟᴀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ ✨\n\n"
        f"🌍 𝐅ʀᴏᴍ: `{source}`\n"
        f"🎯 𝐓ᴏ: `{dest}`\n\n"
        f"📝 {translation.text}"
    )

    await message.reply_text(reply)


@app.on_message(filters.command('tts'))
async def text_to_speech(client, message):
    try:
        if len(message.text.split()) < 2:
            await message.reply_text(
                "❌ 𝐏ʟᴇᴀsᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐓ᴇxᴛ ғᴏʀ 𝐓𝐓𝐒!\n\n"
                "📌 𝐔sᴀɢᴇ: `/tts i love you`"
            )
            return

        text = message.text.split(' ', 1)[1]

        tts = gTTS(text=text, lang='hi')
        file_name = f"speech_{int(time.time())}.mp3"
        tts.save(file_name)

        await app.send_audio(
            chat_id=message.chat.id,
            audio=file_name,
            caption="🎧 𝐇ᴇʀᴇ ɪs ʏᴏᴜʀ 𝐓𝐓𝐒 𝐀ᴜᴅɪᴏ ✨"
        )

        os.remove(file_name)

    except Exception as e:
        await message.reply_text(f"⚠️ 𝐄ʀʀᴏʀ: `{e}`")

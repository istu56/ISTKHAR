from ISTKHAR_MUSIC import app
from config import BOT_USERNAME
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import Unauthorized

# 💾 Temporary Whisper Storage
WHISPER_DB = {}

# 🌸 Start Button
START_BTN = InlineKeyboardMarkup(
    [[InlineKeyboardButton("💖 𝐒ᴛᴀʀᴛ 𝐖ʜɪsᴘᴇʀ 💖", switch_inline_query_current_chat="")]]
)

# ============================= #
# 💌 𝐆ᴇɴᴇʀᴀᴛᴇ 𝐖ʜɪsᴘᴇʀ
# ============================= #

async def build_whisper(client, inline_query):
    query_text = inline_query.query.strip()

    # ❌ If no proper format
    if len(query_text.split()) < 2:
        return [
            InlineQueryResultArticle(
                title="💖 𝐖ʜɪsᴘᴇʀ 💖",
                description=f"@{BOT_USERNAME} [USERNAME/ID] [MESSAGE]",
                input_message_content=InputTextMessageContent(
                    f"💎 𝐔sᴀɢᴇ:\n\n@{BOT_USERNAME} username Your_Message"
                ),
                thumb_url="https://files.catbox.moe/ynsu0c.jpg",
                reply_markup=START_BTN
            )
        ]

    # 🎯 Extract Target + Message
    try:
        target, message = query_text.split(None, 1)
        user = await client.get_users(target)
    except Exception:
        return [
            InlineQueryResultArticle(
                title="❌ 𝐈ɴᴠᴀʟɪᴅ 𝐔sᴇʀ",
                description="Username ya ID galat hai!",
                input_message_content=InputTextMessageContent(
                    "❌ 𝐈ɴᴠᴀʟɪᴅ 𝐔sᴇʀɴᴀᴍᴇ ᴏʀ 𝐈𝐃!"
                ),
                thumb_url="https://files.catbox.moe/ynsu0c.jpg",
                reply_markup=START_BTN
            )
        ]

    # 🔑 Save Whisper
    key = f"{inline_query.from_user.id}_{user.id}"
    WHISPER_DB[key] = message

    # 🔘 Buttons
    normal_btn = InlineKeyboardMarkup(
        [[InlineKeyboardButton(
            "💌 𝐒ʜᴏᴡ 𝐖ʜɪsᴘᴇʀ 💌",
            callback_data=f"whisper_{key}"
        )]]
    )

    one_time_btn = InlineKeyboardMarkup(
        [[InlineKeyboardButton(
            "🔐 𝐎ɴᴇ-𝐓ɪᴍᴇ 𝐖ʜɪsᴘᴇʀ 🔐",
            callback_data=f"whisper_{key}_one"
        )]]
    )

    # 📤 Inline Results
    return [
        InlineQueryResultArticle(
            title="💖 𝐖ʜɪsᴘᴇʀ 💖",
            description=f"𝐒ᴇɴᴅ 𝐚 𝐖ʜɪsᴘᴇʀ 𝐭ᴏ {user.first_name}",
            input_message_content=InputTextMessageContent(
                f"💌 𝐘ᴏᴜ ᴀʀᴇ sᴇɴᴅɪɴɢ ᴀ 𝐖ʜɪsᴘᴇʀ ᴛᴏ {user.first_name}\n\n"
                f"➻ 𝐎ɴʟʏ {user.first_name} ᴄᴀɴ ᴠɪᴇᴡ ᴛʜɪs ᴍᴇssᴀɢᴇ 💎"
            ),
            thumb_url="https://files.catbox.moe/ynsu0c.jpg",
            reply_markup=normal_btn
        ),
        InlineQueryResultArticle(
            title="🔐 𝐎ɴᴇ-𝐓ɪᴍᴇ 𝐖ʜɪsᴘᴇʀ 🔐",
            description=f"𝐒ᴇɴᴅ 𝐚 𝐎ɴᴇ-𝐓ɪᴍᴇ 𝐖ʜɪsᴘᴇʀ 𝐭ᴏ {user.first_name}",
            input_message_content=InputTextMessageContent(
                f"🔐 𝐎ɴᴇ-𝐓ɪᴍᴇ 𝐖ʜɪsᴘᴇʀ ᴛᴏ {user.first_name}\n\n"
                f"➻ 𝐑ᴇᴀᴅ 𝐨ɴᴄᴇ & 𝐚ᴜᴛᴏ 𝐝ᴇʟᴇᴛᴇ 💣"
            ),
            thumb_url="https://files.catbox.moe/ynsu0c.jpg",
            reply_markup=one_time_btn
        )
    ]


# ============================= #
# 🔔 𝐂ᴀʟʟʙᴀᴄᴋ 𝐇ᴀɴᴅʟᴇʀ
# ============================= #

@app.on_callback_query(filters.regex(r"^whisper_"))
async def whisper_callback(client, query):
    data = query.data.split("_")
    from_user = int(data[1])
    to_user = int(data[2])
    user_id = query.from_user.id

    # 🚫 Unauthorized Access
    if user_id not in [from_user, to_user]:
        try:
            await client.send_message(
                from_user,
                f"{query.from_user.mention} 𝐢s 𝐭ʀʏɪɴɢ 𝐭ᴏ ᴏᴘᴇɴ ʏᴏᴜʀ 𝐖ʜɪsᴘᴇʀ 🚧"
            )
        except Unauthorized:
            pass

        return await query.answer(
            "⚠️ 𝐓ʜɪs 𝐖ʜɪsᴘᴇʀ ɪs ɴᴏᴛ ғᴏʀ ʏᴏᴜ!",
            show_alert=True
        )

    key = f"{from_user}_{to_user}"
    message = WHISPER_DB.get(key, "🚫 𝐖ʜɪsᴘᴇʀ 𝐃ᴇʟᴇᴛᴇᴅ!")

    await query.answer(message, show_alert=True)

    # 🗑 One-Time Delete
    if len(data) > 3 and data[3] == "one":
        if user_id == to_user:
            WHISPER_DB.pop(key, None)
            await query.edit_message_text(
                "📬 𝐖ʜɪsᴘᴇʀ 𝐑ᴇᴀᴅ & 𝐃ᴇʟᴇᴛᴇᴅ 💥\n\n"
                "👇 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐓ᴏ 𝐒ᴇɴᴅ 𝐍ᴇᴡ 𝐖ʜɪsᴘᴇʀ",
                reply_markup=START_BTN
            )


# ============================= #
# 🚀 𝐈ɴʟɪɴᴇ 𝐇ᴀɴᴅʟᴇʀ
# ============================= #

@app.on_inline_query()
async def inline_handler(client, inline_query):
    results = await build_whisper(client, inline_query)
    await inline_query.answer(results, cache_time=0)

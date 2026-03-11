from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from ISTKHAR_MUSIC import app
from ISTKHAR_MUSIC.utils.decorators.language import LanguageStart
from config import BANNED_USERS


# =====================================================
# MAIN 9 BUTTON MENU
# =====================================================
def nine_button_menu():
    return InlineKeyboardMarkup(

             [
            [
                InlineKeyboardButton("ᴧᴄᴛɪᴏη", callback_data="vc_help"),
                InlineKeyboardButton("ᴧηᴛɪ-ғʟᴏᴏᴅ", callback_data="music_help"),
                InlineKeyboardButton("ᴧᴘᴘʀᴏᴠᴧʟ", callback_data="queue_help"),
            ],
            [
                InlineKeyboardButton("ᴄʜᴧᴛ-ɢᴘᴛ", callback_data="settings_help"),
                InlineKeyboardButton("ɢɪᴛʜᴜʙ", callback_data="admin_help"),
                InlineKeyboardButton("ɢʀᴏᴜᴘ", callback_data="broadcast_help"),
            ],
            [
                InlineKeyboardButton("sᴛɪᴄᴋᴇʀ", callback_data="stats_help"),
                InlineKeyboardButton("ᴛᴧɢ-ᴧʟʟ", callback_data="db_help"),
                InlineKeyboardButton("ᴛᴏᴏʟs", callback_data="general_help"),
            ],
            [
InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="settings_back_helper")
            ],
        ]
    )


# =====================================================
# OPEN 9 BUTTON MENU (FROM SETTINGS)
# =====================================================
@app.on_callback_query(filters.regex("^9bottonnn$") & ~BANNED_USERS)
@LanguageStart
async def open_nine_menu(client, callback_query: CallbackQuery, _):
    await callback_query.edit_message_text(
        "<blockquote>"
"**📗 ᴅɪᴠᴇ ɪɴᴛᴏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅ ᴄᴀᴛᴇɢᴏʀɪᴇs ʙᴇʟᴏᴡ**\n\n"
"</blockquote>"
"<blockquote>"
"**• ɢᴇᴛ ɢᴜɪᴅᴀɴᴄᴇ - ᴀssɪsᴛᴀɴᴄᴇ ɪɴ ᴏᴜʀ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ](https://t.me/rishu1287) — ɪ'ᴍ ʜᴇʀ𝖾 ғᴏʀ ʏᴏᴜ!**\n"
"</blockquote>"
"<blockquote>"
"**• ᴜsᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴡɪᴛʜ ᴛʜɪs sʏɴᴛᴀx ➜ /**\n" "</blockquote>",
        reply_markup=nine_button_menu(),
    )


# =====================================================
# VC LOGGER
# =====================================================
@app.on_callback_query(filters.regex("^vc_help$") & ~BANNED_USERS)
@LanguageStart
async def vc_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
  ❖ ᴧᴄᴛɪση 
**<u>❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ᴧᴄᴛɪση :</u>**

<u>**❖ ʙᴧη ᴄσϻϻᴧηᴅꜱ ❖**</u>

<blockquote>**❍ /ban : ʙᴧηs ᴧ υsєʀ.
❍ /unban : υηʙᴧηs ᴧ υsєʀ**</blockquote>

<u>**❖ ᴋɪᴄᴋs ᴄσϻϻᴧηᴅꜱ ❖**</u>

<blockquote>**❍ /kick : ᴋɪᴄᴋs υsєʀ συᴛ σғ ɢʀσυᴘ.
❍ /kickme : ᴋɪᴄᴋ ᴛᴏ ʏᴏᴜʀsᴇʟғ σғ ɢʀσυᴘ.**</blockquote>

<u>**❖ ᴡᴀʀɴ ᴄσϻϻᴧηᴅꜱ ❖**</u>

<blockquote>**❍ /warn : ɢɪᴠᴇ ᴡᴀʀɴɪɴɢ ᴀ ᴜsᴇʀ
❍ /rmwarn : ʀᴇᴍᴏᴠᴇ ᴡᴀʀɴɪɴɢ ᴀ ᴜsᴇʀ
❍ /warns : ᴄʜᴇᴄᴋ ᴜsᴇʀ ᴡᴀʀɴ ᴄᴏᴜɴᴛs**</blockquote>

<u>**❖ ᴘʀᴏᴍᴏᴛᴇ ᴄσϻϻᴧηᴅꜱ ❖**</u>

<blockquote>**❍ /promote : ᴘʀᴏᴍᴏᴛᴇ ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ
❍ /demote : ᴅᴇᴍᴏᴛᴇ ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ
❍ /fullpromote : ᴘʀᴏᴍᴏᴛᴇ ᴀᴅᴍɪɴ ғᴜʟʟ ʀɪɢʜᴛs**</blockquote>

<u>**❖ ϻυᴛє ᴄσϻϻᴧηᴅꜱ ❖**</u>

<blockquote>**❍ /mute : ᴍᴜᴛᴇ ᴧ υsєʀ.
❍ /tmute : ᴍυᴛє ᴧ υsєʀ ғσʀ ᴛɪϻє.
❍ /unmute : υηϻυᴛєs ᴧ υsєʀ.**</blockquote>

<blockquote> ᴛʜɪs ᴄσϻϻᴧηᴅ ᴡɪʟʟ ᴡσʀᴋ σηʟʏ ɪғ ʏσυ ɢɪᴠє ʙᴧη ᴏʀ ɴᴇᴡ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ᴛσ ᴛʜє ʙσᴛ ᴡɪᴛʜ ᴧᴅϻɪη.</blockquote>

 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]
            ]
        ),
        disable_web_page_preview=True
    )


# =====================================================
# MUSIC
# =====================================================
@app.on_callback_query(filters.regex("^music_help$") & ~BANNED_USERS)
@LanguageStart
async def music_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
<b>❖ ᴀɴᴛɪ ғʟᴏᴏᴅ ❖</b>
<u>❖ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ꜰᴏʀ ᴀɴᴛɪ ғʟᴏᴏᴅ :</u>

<blockquote><b>❍ /flood</b> : ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴀɴᴛɪғʟᴏᴏᴅ ꜱᴇᴛᴛɪɴɢꜱ
<b>❍ /setflood &lt;number/off/no&gt;</b> : ꜱᴇᴛ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏꜰ ᴄᴏɴꜱᴇᴄᴜᴛɪᴠᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛᴏ ᴛʀɪɢɢᴇʀ ᴀɴᴛɪғʟᴏᴏᴅ
<b>❍ /setfloodtimer &lt;count&gt; &lt;duration&gt;</b> : ᴛɪᴍᴇᴅ ᴀɴᴛɪғʟᴏᴏᴅ
<b>❍ /floodmode &lt;action type&gt;</b> : ᴄʜᴏᴏꜱᴇ ᴀᴄᴛɪᴏɴ (ban/mute/kick/tban/tmute)
<b>❍ /clearflood &lt;yes/no/on/off&gt;</b> : ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇs ᴛʜᴀᴛ ᴛʀɪɢɢᴇʀᴇᴅ ғʟᴏᴏᴅ

<b>Examples:</b>
• /setflood 7 → triggers after 7 messages
• /setflood off → disables anti-flood
• /setfloodtimer 10 30s → 10 messages in 30 seconds
• /setfloodtimer off → disables timed anti-flood
• /floodmode mute → sets action to mute </blockquote>
        """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )


# =====================================================
# QUEUE
# =====================================================
@app.on_callback_query(filters.regex("^queue_help$") & ~BANNED_USERS)
@LanguageStart
async def queue_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
 ❖ ᴀᴘᴘʀᴏᴠᴀʟ ᴍᴏᴅᴇ ❖ 

<blockquote><u>❖ ᴧᴘᴘʀᴏᴠᴀʟ ᴍᴏᴅᴇ ᴛʜʀᴏᴜɢʜ ʙᴜᴛᴛᴏɴ :</u></blockquote>

<blockquote>❍ ᴡʜᴇɴ ᴜsᴇʀ sᴇɴᴅ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛ ʙᴏᴛ sᴇɴᴅ ᴜsᴇʀ ɪɴғᴏ ᴡɪᴛʜ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴ ɪɴ ɢʀᴏᴜᴘ

⋟ ᴏɴʟʏ ᴀᴅᴍɪɴ ᴄᴀɴ ᴀᴘᴘʀᴏᴠᴇ ᴀɴᴅ ᴅɪsᴍɪss ᴀɴᴅ ᴍᴇss ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ɪɴ 10 ᴍɪɴᴜᴛᴇs.</blockquote>
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )


# =====================================================
# SETTINGS
# =====================================================
@app.on_callback_query(filters.regex("^settings_help$") & ~BANNED_USERS)
@LanguageStart
async def settings_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
 ❖ ᴄʜᴧᴛɢᴘᴛ ᴄσϻϻᴧηᴅꜱ ❖ 

<blockquote><u>❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ᴄʜᴧᴛɢᴘᴛ :</u></blockquote>

<blockquote>❖ ᴄʜᴧᴛɢᴘᴛ ᴄσϻϻᴧηᴅs :

❍ /ask : sєᴧʀᴄʜ ᴛʜє ᴧηʏ ᴛʏᴘє ǫυєsᴛɪση.</blockquote>

<blockquote>❖ ɪηѕᴛᴧɢʀᴧϻ ʀєєʟ ᴅᴏᴡηʟᴏᴧᴅ :

❍ /reel : ᴅᴏᴡηʟᴏᴧᴅ ɪηѕᴛᴧɢʀᴧϻ ʀєєʟ.</blockquote>
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )


# =====================================================
# ADMIN
# =====================================================
@app.on_callback_query(filters.regex("^admin_help$") & ~BANNED_USERS)
@LanguageStart
async def admin_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
 ❖ ɢɪᴛʜᴜʙ ᴄσϻϻᴧηᴅꜱ ❖ 

<blockquote><u>❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ɢɪᴛʜᴜʙ :</u></blockquote>

<blockquote>❍ /git : ғɪηᴅ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ.
❍ /allrepo : ᴧʟʟ ʀєᴘᴏ ʙʏ ɢɪᴛ ᴜsєʀηᴧϻє.
❍ /dlrepo : ᴅσᴡηʟσᴧᴅ ᴢɪᴘ ʙʏ ʀєᴘᴏ ᴜʀʟ.</blockquote>
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )


# =====================================================
# GROUP MANAGEMENT
# =====================================================
@app.on_callback_query(filters.regex("^broadcast_help$") & ~BANNED_USERS)
@LanguageStart
async def broadcast_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
 ❖ ɢʀσυᴘ ϻᴧηᴧɢєϻєηᴛ 

<u>❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ɢʀσυᴘ :</u>

<blockquote><u>❖ ᴘɪη/υηᴘɪη ᴄσϻϻᴧηᴅꜱ ❖</u></blockquote>

<blockquote>❍ /pin : ᴘɪηs ᴧ ϻєssᴧɢє.
❍ /pinned : sᴇᴇ ᴘɪηηєᴅ ϻєssᴧɢє.
❍ /unpin : υηᴘɪη ᴘɪηη ϻєssᴧɢє.</blockquote>

<blockquote><u>❖ sᴛᴧғғ/ʙσᴛs ᴄσϻϻᴧηᴅꜱ ❖</u></blockquote>

<blockquote>❍ /staff : ʟɪsᴛ σғ ᴀᴅᴍɪɴs.
❍ /bots : ʟɪsᴛ σғ ʙσᴛs.</blockquote>

<blockquote><u>❖ ɢʀσυᴘ sєᴛ υᴘ ᴄσϻϻᴧηᴅꜱ ❖</u></blockquote>

<blockquote>❍ /settitle : sєᴛ ɴᴀᴍᴇ σғ ɢʀσυᴘ.
❍ /setdis : sєᴛ ʙɪᴏ σғ ɢʀσυᴘ.
❍ /setphoto : sєᴛ ɢʀσυᴘ ᴘʜσᴛσ.
❍ /rmphoto : ʀєϻσᴠє ɢʀσυᴘ ᴘʜσᴛσ.
❍ /unmuteall : ᴜηϻᴜᴛᴇ ᴧʟʟ ϻᴜᴛᴇ ϻєϻʙєʀs.
❍ /unbanall : ᴜηʙᴧη ᴧʟʟ ʙᴧη ϻєϻʙєʀs.
❍ /unpinall : ᴜηᴘɪη ᴧʟʟ ᴘɪη ᴍєssᴧɢᴇ.</blockquote>
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )


# =====================================================
# STATS
# =====================================================
@app.on_callback_query(filters.regex("^stats_help$") & ~BANNED_USERS)
@LanguageStart
async def stats_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
        ❖ sᴛɪᴄᴋєʀs ᴄσϻϻᴧηᴅꜱ ❖
<blockquote>**<u>❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ sᴛɪᴄᴋєʀs :</u>**</blockquote>

<blockquote>**❍ /packkang : ᴄʀєᴧᴛє sᴛɪᴄᴋєʀ ʙʏ σᴛʜєʀ ᴘᴧᴄᴋ.
❍ /stickerid : ɢєᴛ sᴛɪᴄᴋєʀ ɪᴅ σғ sᴛɪᴄᴋєʀ.
❍ /mmf : ʀєᴘʟʏ ᴧηʏ ᴘɪᴄ & ɢɪᴠє ᴛєxᴛ.
❍ /kang : ʀєᴘʟʏ & ᴄʀєᴀᴛє sᴛɪᴄᴋєʀ ᴘᴧᴄᴋ
❍ /st : ғɪηᴅ sᴛɪᴄᴋєʀ ʙʏ ɪᴅ.
❍ /dlsticker : ᴅᴏᴡɴʟᴏᴀᴅ sᴛɪᴄᴋᴇʀ ғɪʟᴇ.
❍ /tiny : ᴄʀᴇᴀᴛᴇ sᴍᴀʟʟ sᴛɪᴄᴋᴇʀ.
❍ /q : ᴄʀєᴧᴛє ϻєssᴧɢє ǫυσᴛє.
❍ /q r : ᴄʀєᴧᴛє ϻєssᴧɢє ǫυσᴛє ᴡɪᴛʜ ʀєᴘʟʏ.</blockquote>
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )


# =====================================================
# DATABASE
# =====================================================
@app.on_callback_query(filters.regex("^db_help$") & ~BANNED_USERS)
@LanguageStart
async def db_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
        ❖ ᴛᴧɢ ᴄσϻϻᴧηᴅꜱ ❖ 
**<u>❖ ᴧᴠᴧɪʟᴧʙʟє ᴄσϻϻᴧηᴅs ꜰσʀ ᴛᴧɢ :</u>**

<blockquote>**✿ ᴄʜσσsє ᴛᴧɢ ɪη ʏσυʀ ᴄʜᴧᴛ ✿</blockquote>

<blockquote>❍ /rtag : ʀᴧηᴅσϻ ᴛᴧɢ ꜱᴛᴧʀᴛ
❍ /rstop : ꜱᴛσᴘ ʀᴧηᴅσϻ ᴛᴧɢ

❍ /vctag : ᴠɪᴅєᴏ ᴄʜᴧᴛ ᴛᴧɢ ꜱᴛᴧʀᴛ
❍ /vstop : ꜱᴛσᴘ ᴠɪᴅєᴏ ᴄʜᴧᴛ ᴛᴧɢ

❍ /gntag : ηɪɢʜᴛ ᴛᴧɢ ꜱᴛᴧʀᴛ
❍ /gnstop : ꜱᴛσᴘ ɢη ᴛᴧɢ

❍ /gmtag : ϻσʀηɪηɢ ᴛᴧɢ ꜱᴛᴧʀᴛ
❍ /gmstop : ꜱᴛᴏᴘ ɢϻ ᴛᴧɢ

❍ /utag : ᴜsᴇʀ ᴛᴧɢ sᴛᴀʀᴛ
❍ /atag : ᴀᴅᴍɪɴ ᴛᴀɢ sᴛᴀʀᴛ
❍ /report : ʀᴇᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs
❍ /cancel : ꜱᴛσᴘ ᴧʟʟ ᴛᴧɢ </blockquote>
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )


# =====================================================
# GENERAL
# =====================================================
@app.on_callback_query(filters.regex("^general_help$") & ~BANNED_USERS)
@LanguageStart
async def general_help(client, cq: CallbackQuery, _):
    await cq.edit_message_text(
        """
        ❖ ᴛᴏᴏʟs ❖ 
<blockquote>**<u>ʜєʀє ɪs ʜєʟᴘ ғσʀ ᴛᴏᴏʟs:</u>**</blockquote>

<blockquote>**❍ /afk : ᴄʀᴇᴀᴛᴇ ᴀ ᴀғᴋ
❍ /couples : sєє ɢʀσᴜᴘs ᴄσᴜᴘʟєs.
❍ /font : ɢᴇɴ sᴛʏʟɪsʜ ғᴏɴᴛ.
❍ /tts : ᴛєxᴛ ᴛσ ᴠσɪᴄє.
❍ /zombies : ᴄʟᴇᴀɴ ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛs.
❍ /mongochk : ᴄʜᴇᴀᴄᴋ ᴍᴏɴɢᴏ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
❍ /tgm : ᴍᴇᴅɪᴀ ᴛᴏ ʟɪɴᴋ.
❍ /tr : ᴛʀᴧηꜱʟᴧᴛє ϻυʟᴛɪᴘʟє ʟᴧηɢυᴧɢєs.
❍ /bug :- ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ғᴏʀ ʙᴜɢ ʀᴇᴘᴏʀᴛ.</blockquote>
""", 
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="9bottonnn")]]
        ),
    )
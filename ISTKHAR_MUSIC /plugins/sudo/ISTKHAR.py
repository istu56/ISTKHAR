import random
from ISTKHAR_MUSIC import app
from ISTKHAR_MUSIC.misc import SUDOERS
from pyrogram import filters
from pyrogram.types import ChatPermissions, Message
from ISTKHAR_MUSIC.utils.ISTKHAR_ban import admin_filter

# ─── Bold Styled Messages ─── #
ISTKHAR_TEXT = [
    "𝐎𝐲𝐞… 𝐝𝐢𝐬𝐭𝐮𝐫𝐛 𝐦𝐚𝐭 𝐤𝐚𝐫, 𝐦𝐚𝐢 𝐬𝐨 𝐫𝐚𝐡𝐚 𝐡𝐮 😴",
    "𝐓𝐮 𝐤𝐨𝐧 𝐡𝐚𝐢 𝐛𝐞? 🤨",
    "𝐀𝐚𝐩 𝐤𝐨𝐧 𝐡𝐨 𝐛𝐡𝐚𝐢? 🤔",
    "𝐀𝐚𝐩 𝐦𝐞𝐫𝐞 𝐨𝐰𝐧𝐞𝐫 𝐧𝐚𝐡𝐢 𝐡𝐨, 𝐬𝐡𝐚𝐚𝐧𝐭 𝐫𝐚𝐡𝐨 🚫",
    "𝐀𝐫𝐞 𝐦𝐞𝐫𝐚 𝐧𝐚𝐚𝐦 𝐤𝐲𝐮 𝐥𝐞 𝐫𝐚𝐡𝐚 𝐡𝐚𝐢? 𝐬𝐨𝐧𝐞 𝐥𝐞 𝐧𝐚 𝐛𝐬𝐝𝐤 😪"
]

STRICT_TEXT = [
    "𝐈 𝐜𝐚𝐧’𝐭 𝐫𝐞𝐬𝐭𝐫𝐢𝐜𝐭 𝐦𝐲 𝐛𝐞𝐬𝐭𝐢𝐞𝐬 — 𝐬𝐚𝐦𝐣𝐡𝐚 𝐤𝐚𝐫 🤝😤",
    "𝐀𝐫𝐞 𝐬𝐞𝐫𝐢𝐨𝐮𝐬𝐥𝐲? 𝐦𝐚𝐢 𝐚𝐩𝐧𝐞 𝐝𝐨𝐬𝐭𝐨𝐧 𝐤𝐨 𝐫𝐞𝐬𝐭𝐫𝐢𝐜𝐭 𝐧𝐚𝐡𝐢 𝐤𝐚𝐫𝐭𝐚 🚫"
]

# ─── Command Lists ─── #
BAN = ["ban", "boom"]
UNBAN = ["unban"]
MUTE = ["mute", "silent", "shut", "fuck"]
UNMUTE = ["unmute", "speak", "free"]
KICK = ["kick", "out", "nikaal", "nikal"]
PROMOTE = ["promote", "adminship"]
FULLPROMOTE = ["fullpromote", "fulladmin"]
DEMOTE = ["demote", "lelo"]

# ─── Main Restriction Handler ─── #
@app.on_message(
    filters.command(["nu", "abu", "anha", "nupriya", "aby"], prefixes=["a","A","b","B","k","K"]) 
    & admin_filter
)
async def restriction_app(client: app, message: Message):
    reply = message.reply_to_message
    chat_id = message.chat.id

    if not reply or len(message.text.split()) < 2:
        return await message.reply(random.choice(ISTKHAR_TEXT))

    commands = message.text.split(maxsplit=1)[1].lower().split()
    user_id = reply.from_user.id

    for cmd in commands:
        print(f"⚡ Processing command: {cmd}")

        # ── BAN ── #
        if cmd in BAN:
            if user_id in SUDOERS:
                await message.reply(random.choice(STRICT_TEXT))
            else:
                await client.ban_chat_member(chat_id, user_id)
                await message.reply("🔨 𝐁𝐚𝐧 𝐭𝐡𝐨𝐤 𝐝𝐢𝐚! 𝐙𝐲𝐚𝐝𝐚 𝐛𝐚𝐤𝐜𝐡𝐨𝐝𝐢 𝐤𝐚𝐫 𝐫𝐚𝐡𝐚 𝐭𝐡𝐚.")

        # ── UNBAN ── #
        elif cmd in UNBAN:
            await client.unban_chat_member(chat_id, user_id)
            await message.reply("✅ 𝐔𝐧𝐛𝐚𝐧 𝐤𝐚𝐫 𝐝𝐢𝐚.")

        # ── KICK ── #
        elif cmd in KICK:
            if user_id in SUDOERS:
                await message.reply(random.choice(STRICT_TEXT))
            else:
                await client.ban_chat_member(chat_id, user_id)
                await client.unban_chat_member(chat_id, user_id)
                await message.reply("👋 𝐆𝐞𝐭 𝐥𝐨𝐬𝐭! 𝐎𝐮𝐭.")

        # ── MUTE ── #
        elif cmd in MUTE:
            if user_id in SUDOERS:
                await message.reply(random.choice(STRICT_TEXT))
            else:
                permissions = ChatPermissions(can_send_messages=False)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply("🔇 𝐌𝐮𝐭𝐞𝐝 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲! 𝐂𝐚𝐧'𝐭 𝐭𝐨𝐥𝐞𝐫𝐚𝐭𝐞 𝐛𝐚𝐤𝐜𝐡𝐨𝐝𝐢.")

        # ── UNMUTE ── #
        elif cmd in UNMUTE:
            permissions = ChatPermissions(can_send_messages=True)
            await message.chat.restrict_member(user_id, permissions)
            await message.reply("🎤 𝐔𝐧𝐦𝐮𝐭𝐞𝐝! 𝐒𝐩𝐞𝐚𝐤 𝐟𝐫𝐞𝐞𝐥𝐲.")

        # ── PROMOTE ── #
        elif cmd in PROMOTE:
            await client.promote_chat_member(
                chat_id, user_id,
                privileges=ChatPrivileges(
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_pin_messages=True,
                    can_manage_chat=True,
                    can_manage_video_chats=True
                )
            )
            await message.reply("🚀 𝐏𝐫𝐨𝐦𝐨𝐭𝐞𝐝!")

        # ── FULL PROMOTE ── #
        elif cmd in FULLPROMOTE:
            await client.promote_chat_member(
                chat_id, user_id,
                privileges=ChatPrivileges(
                    can_change_info=True,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=True,
                    can_pin_messages=True,
                    can_promote_members=True,
                    can_manage_chat=True,
                    can_manage_video_chats=True
                )
            )
            await message.reply("💎 𝐅𝐮𝐥𝐥 𝐏𝐫𝐨𝐦𝐨𝐭𝐞𝐝!")

        # ── DEMOTE ── #
        elif cmd in DEMOTE:
            await client.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges())
            await message.reply("🔻 𝐃𝐞𝐦𝐨𝐭𝐞𝐝!")

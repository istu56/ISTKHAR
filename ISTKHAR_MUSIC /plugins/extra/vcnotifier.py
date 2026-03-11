from typing import List, Optional, Union
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import ChatPrivileges, Message

from ISTKHAR_MUSIC import app
from ISTKHAR_MUSIC.utils.database import get_assistant

# ---------------------------------------------------------
# 🔥 Command Helper
# ---------------------------------------------------------
def command(commands: Union[str, List[str]]):
    return filters.command(commands, prefixes=["/", "!"])

# ---------------------------------------------------------
# 🎧 Get Active Voice Chat
# ---------------------------------------------------------
async def get_group_call(assistant: Client, message: Message, err_msg: str = "") -> Optional[InputGroupCall]:
    chat_peer = await assistant.resolve_peer(message.chat.id)
    full_chat = None
    if isinstance(chat_peer, InputPeerChannel):
        full_chat = (await assistant.invoke(GetFullChannel(channel=chat_peer))).full_chat
    elif isinstance(chat_peer, InputPeerChat):
        full_chat = (await assistant.invoke(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
    if full_chat and full_chat.call:
        return full_chat.call

    await app.send_message(
        message.chat.id,
        f"❌ 𝐍ᴏ 𝐀𝐂𝐓𝐈ᴠᴇ 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ {err_msg}"
    )
    return None

# ---------------------------------------------------------
# 🚀 START VOICE CHAT
# ---------------------------------------------------------
@app.on_message(command(["vcstart", "startvc"]) & filters.group)
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    if not assistant:
        return await app.send_message(chat_id, "❌ 𝐀𝐬𝐬ɪsᴛ𝐚ɴᴛ 𝐍ᴏᴛ 𝐅𝐨ᴜɴᴅ")

    ass = await assistant.get_me()
    assid = ass.id

    msg = await app.send_message(chat_id, "🎙 𝐒ᴛ𝐚ʀᴛɪɴɢ 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ...\n━━━━━━━━━━━━━━")

    try:
        peer = await assistant.resolve_peer(chat_id)
        await assistant.invoke(
            CreateGroupCall(
                peer=InputPeerChannel(channel_id=peer.channel_id, access_hash=peer.access_hash),
                random_id=assistant.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("✅ 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ 𝐒ᴛ𝐚ʀᴛᴇᴅ 👑")

    except ChatAdminRequired:
        try:
            # Temporary Promote
            await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(can_manage_video_chats=True))
            peer = await assistant.resolve_peer(chat_id)
            await assistant.invoke(
                CreateGroupCall(peer=InputPeerChannel(channel_id=peer.channel_id, access_hash=peer.access_hash),
                                random_id=assistant.rnd_id() // 9000000000)
            )
            # Remove permission
            await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(can_manage_video_chats=False))
            await msg.edit_text("✅ 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ 𝐒ᴛ𝐚ʀᴛᴇᴅ 👑")
        except:
            await msg.edit_text("❌ 𝐏ʟᴇᴀsᴇ 𝐆ɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜ𝐚ᴛ 𝐏ᴇʀᴍɪssɪᴏɴ 𝐓ᴏ 𝐁ᴏᴛ")

# ---------------------------------------------------------
# 🛑 END VOICE CHAT
# ---------------------------------------------------------
@app.on_message(command(["vcend", "endvc"]) & filters.group)
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    assistant = await get_assistant(chat_id)
    if not assistant:
        return await app.send_message(chat_id, "❌ 𝐀𝐬𝐬ɪsᴛ𝐚ɴᴛ 𝐍ᴏᴛ 𝐅𝐨ᴜɴᴅ")

    ass = await assistant.get_me()
    assid = ass.id

    msg = await app.send_message(chat_id, "🔻 𝐄ɴᴅɪɴɢ 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ...\n━━━━━━━━━━━━━━")

    try:
        group_call = await get_group_call(assistant, m, err_msg="• Already Ended")
        if not group_call:
            return
        await assistant.invoke(DiscardGroupCall(call=group_call))
        await msg.edit_text("🛑 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ 𝐄ɴᴅᴇᴅ 👑")
    except Exception as e:
        if "GROUPCALL_FORBIDDEN" in str(e):
            try:
                await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(can_manage_video_chats=True))
                group_call = await get_group_call(assistant, m, err_msg="• Already Ended")
                if not group_call:
                    return
                await assistant.invoke(DiscardGroupCall(call=group_call))
                await app.promote_chat_member(chat_id, assid, privileges=ChatPrivileges(can_manage_video_chats=False))
                await msg.edit_text("🛑 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ 𝐄ɴᴅᴇᴅ 👑")
            except:
                await msg.edit_text("❌ 𝐏ʟᴇᴀsᴇ 𝐆ɪᴠᴇ 𝐕ɪᴅᴇᴏ 𝐂ʜ𝐚ᴛ 𝐏ᴇʀᴍɪssɪᴏɴ 𝐓ᴏ 𝐁ᴏᴛ")

# ---------------------------------------------------------
# 🎥 AUTO DETECT - VC STARTED
# ---------------------------------------------------------
@app.on_message(filters.video_chat_started & filters.group)
async def auto_vc_started(client: Client, message: Message):
    await message.reply_text(
        f"> 🎥 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ 𝐈𝐬 𝐍ᴏᴡ 𝐋ɪᴠᴇ 👑\n"
        f"> 🏷 {message.chat.title}\n"
        f"> ⚡ Join Now & Enjoy The Session!"
    )

# ---------------------------------------------------------
# 🚫 AUTO DETECT - VC ENDED
# ---------------------------------------------------------
@app.on_message(filters.video_chat_ended & filters.group)
async def auto_vc_ended(client: Client, message: Message):
    await message.reply_text(
        f"> 🛑 𝐕ᴏɪᴄᴇ 𝐂ʜ𝐚ᴛ 𝐇ᴀs 𝐄ɴᴅᴇᴅ 👋\n"
        f"> 🏷 {message.chat.title}\n"
        f"> 🔥 See You In Next Session!"
    )

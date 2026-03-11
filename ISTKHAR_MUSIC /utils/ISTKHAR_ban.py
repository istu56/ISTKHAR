from pyrogram import filters
from ISTKHAR_MUSIC.utils.admin_check import admin_check
from ISTKHAR_MUSIC.misc import SUDOERS


def sudo_filter_func(_, __, message):
    return bool(
        message.from_user
        and message.from_user.id in SUDOERS
        and not message.edit_date
    )


sudo_filter = filters.create(sudo_filter_func)


async def admin_filter_func(_, __, message):
    return not message.edit_date and await admin_check(message)


admin_filter = filters.create(admin_filter_func)

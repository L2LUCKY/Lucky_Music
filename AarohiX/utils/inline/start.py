from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 ᴏᴜʀ ɢʀᴏᴜᴩ 🥰",
                url=f"https://t.me/+WDNH4yTCWe5jOTI1",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ ʜᴇʟᴩ ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥 sᴇᴛᴛɪɴɢs ❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔥 ᴏᴡɴᴇʀ 🔥", url=f"https://t.me/itz_Lucky_Raja"),
            InlineKeyboardButton(
                text="😍 ᴄᴏ ᴏᴡɴᴇʀ 😍", url=f"https://t.me/Sonu2860"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥 Bᴀᴅsʜᴀʜ ❤️‍🔥", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰 sᴜᴩᴩᴏʀᴛ 🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🥺",
                url=f"https://t.me/+WDNH4yTCWe5jOTI1",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺 ʜᴇʟᴩ 🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔥 ᴏᴡɴᴇʀ 🔥", url=f"https://t.me/itz_Lucky_Raja"),
            InlineKeyboardButton(
                text="😍 ᴄᴏ ᴏᴡɴᴇʀ 😍", url=f"https://t.me/Sonu2860"
            ),
        ],
        [
            InlineKeyboardButton(text="❤️‍🔥 Bᴀᴅsʜᴀʜ ❤️‍🔥", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰 sᴜᴩᴩᴏʀᴛ 🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥰 ᴍᴏʀᴇ 🥰", url=f"https://t.me/ZiddiXBot"
            ),
           ],
     ]
    return buttons



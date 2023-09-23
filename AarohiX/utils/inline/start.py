from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 Oᴜʀ Gʀᴏᴜᴩ 🥰",
                url=f"https://t.me/+WDNH4yTCWe5jOTI1",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ Hᴇʟᴩ ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥 Sᴇᴛᴛɪɴɢs ❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥 Bᴀᴅsʜᴀʜ ❤️‍🔥", url=f"https://t.me/Shivans_Raj_BrockenHart"),
            InlineKeyboardButton(
                text="🥰 Sᴜᴩᴩᴏʀᴛ 🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                text="🔥 Oᴡɴᴇʀ 🔥", user_id=OWNER),
            InlineKeyboardButton(
                text="😍 Cᴏ Oᴡɴᴇʀ 😍", url=f"https://t.me/MR_Manu_Tiwari"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 Oᴜʀ Gʀᴏᴜᴩ 🥰",
                url=f"https://t.me/+WDNH4yTCWe5jOTI1",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺 Hᴇʟᴩ 🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥 Bᴀᴅsʜᴀʜ ❤️‍🔥", url=f"https://t.me/Shivans_Raj_BrockenHart"),
            InlineKeyboardButton(
                text="🥰 Sᴜᴩᴩᴏʀᴛ 🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(text="🔥 Oᴡɴᴇʀ 🔥", user_id=OWNER),
            InlineKeyboardButton(
                text="😍 Cᴏ Oᴡɴᴇʀ 😍", url=f"https://t.me/MR_Manu_Tiwari"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="😂 Mᴏʀᴇ 😂", url=f"https://t.me/ZiddiXBot"
            ),
           ],
     ]
    return buttons



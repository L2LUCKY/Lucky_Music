from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 𝐎ᴜʀ 𝐆ʀᴏᴜᴩ 🥰",
url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="🥹 𝐇ᴇʟᴩ 🥹",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="😂 𝐒ᴇᴛᴛɪɴɢ𝐬 😂", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐎ᴡɴᴇʀ 💖", user_id=OWNER),
            InlineKeyboardButton(
                text="💝 𝐂ᴏ 𝐎ᴡɴᴇʀ 💝", url=f"https://t.me/MR_RAJA_ROY"
             ),
        ],
        [
            InlineKeyboardButton(
                text="❣️ 𝐀𝐀𝐑𝐔 ❣️", url=f"https://t.me/Notanki_aaru"),
            InlineKeyboardButton(
                text="❤️ 𝐇ᴇᴀʀᴛ♡𝐇ᴀᴄᴋᴇʀ ❤️", url=f"https://t.me/Hacker_girl59"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥰 𝐎ᴜʀ 𝐆ʀᴏᴜᴩ 🥰",
url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥹 𝐇ᴇʟᴩ 🥹", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐎ᴡɴᴇʀ 💖", user_id=OWNER),
            InlineKeyboardButton(
                text="💝 𝐂ᴏ 𝐎ᴡɴᴇʀ 💝", url=f"https://t.me/MR_RAJA_ROY"
            ),
        ],
        [
            InlineKeyboardButton(text="❣️ 𝐀𝐀𝐑𝐔 ❣️", url=f"https://t.me/Notanki_aaru"),
            InlineKeyboardButton(
                text="❤️ 𝐇ᴇᴀʀᴛ♡𝐇ᴀᴄᴋᴇʀ ❤️", url=f"https://t.me/Hacker_girl59"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🌹 𝐒ᴛᴜᴅʏ 𝐆ʀᴏᴜᴘ  🌹", url=f"https://t.me/Study_House_Family"
            ),
           ],
     ]
    return buttons



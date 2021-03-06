#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        

                [InlineKeyboardButton("ðķðūðĪðĒðĒððĢððĻðĪ", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "âĪïļðūâððâðĪ", url=f"https://t.me/Urban_Chat_Group"

                    ),

                    InlineKeyboardButton(

                        "âĪïļðūðð―ðīððĪ", url=f"https://t.me/PB_65_Aujla"

                    ),

                ],
    ]
    
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
       [

                    InlineKeyboardButton(

                        "ð ðžðŋðŋ ðð ðð ðððð ððððð ðĪ",

                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",

                    )

                ],

                [InlineKeyboardButton("ðķðūðĪðĒðĒððĢððĻðĪ", url=f"https://telegra.ph/Aujla-Music-Commands-03-18")],

                







                [

                    InlineKeyboardButton(

                        "ðððĄððĪððĪš", url=f"https://t.me/Urban_Chat_Group"

                    ),

                    InlineKeyboardButton(

                        "ðĨðĒðĨððĨðĶðĪðĨ", url=f"https://t.me/Punjabi_Status_Mania"

                    ),

                ],
        [InlineKeyboardButton("ðŪðģ ðððĢððŠððð ð", callback_data="LG")],
    ]
  
    return buttons

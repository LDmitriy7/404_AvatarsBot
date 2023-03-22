from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import commands
from loader import texts


class MenuKeyboard(InlineKeyboardMarkup):
    ANIME_AVATARS = InlineKeyboardButton("⛩ Аниме авы", callback_data=0)
    PAIRED_AVATARS = InlineKeyboardButton("🎎 Парные аватарки", callback_data=0)
    CUTE_PICTURES = InlineKeyboardButton("💖 Милые пикчи", callback_data=0)
    ANGRY_PICTURES = InlineKeyboardButton("😡 Агрессивные", callback_data=0)

    buttons = [
        [ANIME_AVATARS, PAIRED_AVATARS],
        [CUTE_PICTURES, ANGRY_PICTURES],
    ]

    def __init__(self, startgroup_url: str) -> None:
        button = InlineKeyboardButton("💬 Добавить в чат", url=startgroup_url)
        buttons = [*self.buttons, [button]]
        super().__init__(buttons)


class Texts:
    wait = texts[1]
    required_join = texts[2]
    private_welcome = texts[3]
    group_welcome = texts[4].format(
        commands.GET_AVATARS,
        commands.GET_PAIRED,
        commands.GET_CUTE,
        commands.GET_ANGRY,
        commands.SEND_PICTURE,
    )

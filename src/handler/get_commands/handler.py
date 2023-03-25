from botty import CommandHandler, CompositeHandler

import commands
from assets import PictureCategory


class _Handler(CommandHandler):
    def __init__(self, category: str, command: str) -> None:
        self.reply_text = category
        super().__init__(command)


handler = CompositeHandler(
    _Handler(PictureCategory.AVATAR, commands.GET_AVATARS),
    _Handler(PictureCategory.PAIRED_AVATARS, commands.GET_PAIRED),
    _Handler(PictureCategory.CUTE, commands.GET_CUTE),
    _Handler(PictureCategory.ANGRY, commands.GET_ANGRY),
)

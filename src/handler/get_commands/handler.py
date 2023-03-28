from botty import CommandHandler, CompositeHandler

import commands
from assets import PictureCategory


class Handler(CommandHandler):
    def __init__(self, command: str, category: str) -> None:
        super().__init__(command, category)


handler = CompositeHandler(
    Handler(commands.GET_AVATARS, PictureCategory.AVATAR),
    Handler(commands.GET_PAIRED, PictureCategory.PAIRED_AVATARS),
    Handler(commands.GET_CUTE, PictureCategory.CUTE),
    Handler(commands.GET_ANGRY, PictureCategory.ANGRY),
)

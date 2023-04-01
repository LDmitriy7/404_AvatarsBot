from botty import CommandsHandler

from lib import PictureCallback, PictureCategory, commands

_handlers = {
    commands.GET_AVATARS: PictureCallback(PictureCategory.AVATAR),
    commands.GET_PAIRED: PictureCallback(PictureCategory.PAIRED_AVATARS),
    commands.GET_CUTE: PictureCallback(PictureCategory.CUTE),
    commands.GET_ANGRY: PictureCallback(PictureCategory.ANGRY),
}

handler = CommandsHandler(_handlers)

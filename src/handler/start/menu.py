from botty import InlineMenuHandler

from lib import MenuKeyboard, PictureCallback, PictureCategory

_handlers = {
    MenuKeyboard.AVATAR: PictureCallback(PictureCategory.AVATAR),
    MenuKeyboard.PAIRED_AVATARS: PictureCallback(PictureCategory.PAIRED_AVATARS),
    MenuKeyboard.CUTE: PictureCallback(PictureCategory.CUTE),
    MenuKeyboard.ANGRY: PictureCallback(PictureCategory.ANGRY),
}

handler = InlineMenuHandler(_handlers)

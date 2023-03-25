from botty import InlineMenuHandler

from . import subhandlers
from .assets import Keyboard

handler = InlineMenuHandler(
    {
        Keyboard.AVATAR: subhandlers.avatar_handler,
        Keyboard.PAIRED_AVATARS: subhandlers.paired_avatars_handler,
        Keyboard.CUTE: subhandlers.cute_picture_handler,
        Keyboard.ANGRY: subhandlers.angry_picture_handler,
    },
)

from botty import InlineMenuHandler

from assets import MenuKeyboard

from .subhandlers import Subhandlers

buttons = {
    MenuKeyboard.AVATAR: Subhandlers.AVATAR,
    MenuKeyboard.PAIRED_AVATARS: Subhandlers.PAIRED_AVATARS,
    MenuKeyboard.CUTE: Subhandlers.CUTE_PICTURE,
    MenuKeyboard.ANGRY: Subhandlers.ANGRY_PICTURE,
}

handler = InlineMenuHandler(buttons)

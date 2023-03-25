from botty.buttons import CallbackButton, UrlButton
from botty.keyboards import InlineButtons, InlineKeyboard

from loader import texts


class Keyboard(InlineKeyboard):
    AVATAR = CallbackButton(texts[5])
    PAIRED_AVATARS = CallbackButton(texts[6])
    CUTE = CallbackButton(texts[7])
    ANGRY = CallbackButton(texts[8])

    def __init__(self, startgroup_url: str) -> None:
        self._startgroup_url = startgroup_url

    def get_buttons(self) -> InlineButtons:
        return [
            [self.AVATAR, self.PAIRED_AVATARS],
            [self.CUTE, self.ANGRY],
            [UrlButton(texts[9], self._startgroup_url)],
        ]

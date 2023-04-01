from botty import CallbackButton, InlineKeyboard, UrlButton, texts


class MenuKeyboard(InlineKeyboard):
    AVATAR = CallbackButton(texts[5])
    PAIRED_AVATARS = CallbackButton(texts[6])
    CUTE = CallbackButton(texts[7])
    ANGRY = CallbackButton(texts[8])

    buttons = [
        [AVATAR, PAIRED_AVATARS],
        [CUTE, ANGRY],
    ]

    def __init__(self, startgroup_url: str) -> None:
        super().__init__(*self.buttons, [UrlButton(texts[9], startgroup_url)])


class AdminKeyboard(InlineKeyboard):
    BROADCAST = CallbackButton(texts[15])
    REQUIRED_JOIN = CallbackButton(texts[16])

    buttons = [
        [BROADCAST],
        [REQUIRED_JOIN],
    ]

    def __init__(self) -> None:
        super().__init__(*self.buttons)

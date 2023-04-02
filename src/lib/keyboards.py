from botty import CallbackButton, InlineKeyboard, ReplyKeyboard, UrlButton, texts

CANCEL_BUTTON = CallbackButton(texts[18])
CONFIRM_BUTTON = CallbackButton(texts[20])


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
        footer = [UrlButton(texts[9], startgroup_url)]
        super().__init__(*self.buttons, footer)


class AdminKeyboard(InlineKeyboard):
    BROADCAST = CallbackButton(texts[15])
    REQUIRED_JOIN = CallbackButton(texts[16])

    buttons = [
        [BROADCAST],
        [REQUIRED_JOIN],
    ]


class CancelKeyboard(InlineKeyboard):
    buttons = [[CANCEL_BUTTON]]


class ConfirmKeyboard(InlineKeyboard):
    buttons = [
        [CONFIRM_BUTTON],
        [CANCEL_BUTTON],
    ]


class PictureKeyboard(ReplyKeyboard):
    GET_ANOTHER = texts[23]
    MAIN_MENU = texts[24]

    buttons = [[GET_ANOTHER, MAIN_MENU]]

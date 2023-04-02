from botty import InlineMenuHandler, MessageContext

from lib import MenuKeyboard, PictureCallback, PictureCategory, PictureKeyboard, keys


class Callback(PictureCallback):
    def __init__(self, category: str) -> None:
        super().__init__(category, PictureKeyboard())

    async def __call__(self, ctx: MessageContext) -> None:
        ctx.storage[keys.CATEGORY] = self._category
        await super().__call__(ctx)


_handlers = {
    MenuKeyboard.AVATAR: Callback(PictureCategory.AVATAR),
    MenuKeyboard.PAIRED_AVATARS: Callback(PictureCategory.PAIRED_AVATARS),
    MenuKeyboard.CUTE: Callback(PictureCategory.CUTE),
    MenuKeyboard.ANGRY: Callback(PictureCategory.ANGRY),
}

handler = InlineMenuHandler(_handlers)

from botty import TextContext, TextHandler, texts

from lib import PictureCallback, PictureCategory

TRIGGERS = {
    PictureCategory.AVATAR: texts.get_words(10),
    PictureCategory.PAIRED_AVATARS: texts.get_words(11),
    PictureCategory.CUTE: texts.get_words(12),
    PictureCategory.ANGRY: texts.get_words(13),
}


async def callback(ctx: TextContext) -> None:
    for word in ctx.text_words:
        for category, triggers in TRIGGERS.items():
            if word in triggers:
                await PictureCallback(category)(ctx)
                return


handler = TextHandler(callback)

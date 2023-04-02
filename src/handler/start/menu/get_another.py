from botty import TextContext, TextHandler

from lib import PictureCallback, PictureKeyboard, keys


async def callback(ctx: TextContext) -> None:
    await PictureCallback(ctx.storage[keys.CATEGORY])(ctx)


handler = TextHandler(callback, PictureKeyboard.GET_ANOTHER)

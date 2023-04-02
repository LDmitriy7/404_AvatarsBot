from botty import CompositeHandler, StartGroupHandler, StartHandler, TextContext

from lib import menu_callback, texts


async def callback(ctx: TextContext) -> None:
    await ctx.reply(texts.GROUP_WELCOME)


handler = CompositeHandler(
    StartGroupHandler(callback),
    StartHandler(menu_callback),
)

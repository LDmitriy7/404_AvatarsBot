from botty import CompositeHandler, StartGroupHandler, StartHandler, TextContext

from lib import MenuKeyboard, texts


async def start_callback(ctx: TextContext) -> None:
    text = texts.PRIVATE_WELCOME.format(ctx.user.mention)
    keyboard = MenuKeyboard(ctx.bot.startgroup_url)
    await ctx.reply(text, keyboard)


async def start_group_callback(ctx: TextContext) -> None:
    await ctx.reply(texts.GROUP_WELCOME)


handler = CompositeHandler(
    StartGroupHandler(start_group_callback),
    StartHandler(start_callback),
)

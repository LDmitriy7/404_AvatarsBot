from botty import CommandHandler, TextContext

from lib import AdminKeyboard, commands, texts


async def callback(ctx: TextContext) -> None:
    await ctx.reply(texts.ADMIN_PANEL, AdminKeyboard())


handler = CommandHandler(commands.ADMIN, callback)

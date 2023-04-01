from botty import CommandHandler, TextContext

from lib import commands, texts


async def callback(ctx: TextContext) -> None:
    await ctx.reply(texts.DOES_NOT_WORK)


handler = CommandHandler(commands.SEND_PICTURE, callback)

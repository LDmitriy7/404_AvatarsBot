from botty import MessageContext, ReplyKeyboard, TextContext

from . import texts
from .keyboards import MenuKeyboard


class PictureCallback:  # TODO
    def __init__(self, category: str, markup: ReplyKeyboard | None = None) -> None:
        self._category = category
        self._markup = markup

    async def __call__(self, ctx: MessageContext) -> None:
        await ctx.reply(self._category, self._markup)


async def menu_callback(ctx: TextContext) -> None:
    text = texts.PRIVATE_WELCOME.format(ctx.user.mention)
    keyboard = MenuKeyboard(ctx.bot.startgroup_url)
    await ctx.reply(text, keyboard)

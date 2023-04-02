from botty import QueryContext, QueryHandler

from lib import CANCEL_BUTTON, AdminKeyboard, keys, texts


async def callback(ctx: QueryContext) -> int:
    await ctx.edit(texts.ADMIN_PANEL, AdminKeyboard())
    return keys.END


handler = QueryHandler(CANCEL_BUTTON, callback)

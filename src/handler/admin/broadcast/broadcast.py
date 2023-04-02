from botty import QueryContext, QueryHandler

from lib import AdminKeyboard, CancelKeyboard, keys, texts


async def callback(ctx: QueryContext) -> int:
    await ctx.edit(texts.ASK_POST, CancelKeyboard())
    return keys.POST


handler = QueryHandler(AdminKeyboard.BROADCAST, callback)

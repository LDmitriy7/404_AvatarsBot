from botty import QueryContext, QueryHandler

from lib import CONFIRM_BUTTON, keys, texts


async def callback(ctx: QueryContext) -> int:
    await ctx.edit(texts.STARTING_BROADCAST)
    await ctx.copy(ctx.storage[keys.POST_ID])
    return keys.END  # TODO


handler = QueryHandler(CONFIRM_BUTTON, callback)

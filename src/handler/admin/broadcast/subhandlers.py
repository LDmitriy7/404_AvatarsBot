from botty import QueryContext, QueryHandler

from lib import AdminKeyboard


async def callback(ctx: QueryContext) -> None:
    await ctx.answer("broadcast")


entry_handler = QueryHandler(AdminKeyboard.BROADCAST, callback)

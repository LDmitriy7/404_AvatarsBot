from botty import UpdateContext


class PictureCallback:
    def __init__(self, category: str) -> None:
        self._category = category

    async def __call__(self, ctx: UpdateContext) -> None:
        await ctx.reply(self._category)

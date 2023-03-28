from botty import QueryHandler

from assets import PictureCategory


class PictureHandler(QueryHandler):
    def __init__(self, category: str) -> None:
        self.category = category
        super().__init__()

    async def callback(self) -> None:
        await self.answer(self.category)


class Subhandlers:
    AVATAR = PictureHandler(PictureCategory.AVATAR)
    PAIRED_AVATARS = PictureHandler(PictureCategory.PAIRED_AVATARS)
    CUTE_PICTURE = PictureHandler(PictureCategory.CUTE)
    ANGRY_PICTURE = PictureHandler(PictureCategory.ANGRY)

from botty import QueryHandler

from assets import PictureCategory


class PictureHandler(QueryHandler):
    def __init__(self, category: str) -> None:
        self.category = category
        super().__init__()

    async def callback(self) -> None:
        await self.answer(self.category)


avatar_handler = PictureHandler(PictureCategory.AVATAR)
paired_avatars_handler = PictureHandler(PictureCategory.PAIRED_AVATARS)
cute_picture_handler = PictureHandler(PictureCategory.CUTE)
angry_picture_handler = PictureHandler(PictureCategory.ANGRY)

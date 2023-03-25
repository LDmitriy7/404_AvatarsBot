from botty import TextHandler

from .assets import TRIGGERS_TO_CATEGORY


class _Handler(TextHandler):
    async def callback(self) -> None:
        words = self.text.lower().split()

        for triggers, category in TRIGGERS_TO_CATEGORY:
            for word in words:
                if word in triggers:
                    await self.reply(category)
                    break


handler = _Handler()

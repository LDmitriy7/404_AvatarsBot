from botty import CompositeHandler

from core import StartGroupHandler, StartHandler
from handler.start import menu

from .assets import Texts


class _Handler(StartHandler):
    async def prepare(self) -> None:
        mention = self.user.mention
        self.reply_text = self.reply_text.format(mention)
        self.reply_keyboard = menu.Keyboard(self.bot.startgroup_url)


handler = CompositeHandler(
    StartGroupHandler(Texts.group_welcome),
    _Handler(Texts.private_welcome),
)

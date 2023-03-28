from botty import CompositeHandler, StartGroupHandler, StartHandler

from assets import MenuKeyboard

from .assets import Texts


class Handler(StartHandler):
    def get_reply_text(self) -> str:
        return Texts.private_welcome.format(self.user.mention)

    def get_reply_keyboard(self) -> MenuKeyboard:
        return MenuKeyboard(self.bot.startgroup_url)


handler = CompositeHandler(
    StartGroupHandler(Texts.group_welcome),
    Handler(),
)

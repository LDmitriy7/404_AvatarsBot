import core
from assets import MenuKeyboard, Texts


class StartHandler(core.StartHandler):
    reply_text = Texts.group_welcome
    reply_markup = None

    async def callback(self) -> None:
        self.prepare()
        await super().callback()

    def prepare(self) -> None:
        if self.chat.is_group:
            return

        mention = self.user.mention
        self.reply_text = Texts.private_welcome.format(mention)
        self.reply_markup = MenuKeyboard(self.bot.startgroup_url)

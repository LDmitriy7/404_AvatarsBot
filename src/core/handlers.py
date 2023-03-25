import botty
from telegram import ext


class CommandHandler(botty.CommandHandler):
    reply_text: str

    def __init__(self, command: str, text: str) -> None:
        self.reply_text = text
        super().__init__(command)


class StartHandler(botty.StartHandler):
    reply_text: str
    reply_keyboard: botty.InlineKeyboard

    def __init__(self, text: str) -> None:
        self.reply_text = text
        super().__init__()

    async def callback(self) -> None:
        self.reply_markup = self.reply_keyboard.build()
        await super().callback()


class StartGroupHandler(botty.StartHandler):
    filters = botty.StartHandler.filters & ext.filters.ChatType.GROUPS

    def __init__(self, text: str) -> None:
        self.reply_text = text
        super().__init__()

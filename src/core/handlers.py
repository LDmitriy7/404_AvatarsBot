from typing import Never

import botty
from botty.handlers.classes.update import UpdateFieldError
from botty.handlers.types import ReplyMarkup

from .classes import Bot, Chat, User


class StartHandler(botty.StartHandler):
    reply_text: str
    reply_markup: ReplyMarkup | None = None

    async def callback(self) -> None:
        self._validate_field("reply_text")
        await self.reply(self.reply_text, self.reply_markup)

    @property
    def chat(self) -> Chat:
        return Chat(self.message.chat)

    @property
    def user(self) -> User:
        raw = self.message.from_user
        if raw is None:
            self._raise_field_error("user")
        return User(raw)

    def _raise_field_error(self, field: str) -> Never:
        raise UpdateFieldError(self.update, field)

    @property
    def bot(self) -> Bot:
        raw = self.context.bot
        return Bot(raw)

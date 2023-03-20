import warnings

from telegram.ext import Application
from telegram.warnings import PTBUserWarning

from handler import Handler

warnings.filterwarnings(
    action="ignore",
    message=".* should be built via the `ApplicationBuilder`",
    category=PTBUserWarning,
)


class App:
    def __init__(self, token: str) -> None:
        self.raw = Application.builder().token(token).build()

    def run(self, handlers: list[type[Handler]]) -> None:
        for handler in handlers:
            self.raw.add_handler(handler.build())
        self.raw.run_polling()

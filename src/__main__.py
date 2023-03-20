import os

from app import App
from handler import Handler

TOKEN = os.environ["BOT_TOKEN"]


class StartHandler(Handler):
    on_command = "start"

    async def callback(self) -> None:
        await self.reply("Hello")


app = App(TOKEN)
app.run([StartHandler])

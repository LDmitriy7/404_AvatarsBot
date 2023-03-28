from botty import CommandHandler

import commands

from .assets import Texts

handler = CommandHandler(commands.SEND_PICTURE, Texts.does_not_work)

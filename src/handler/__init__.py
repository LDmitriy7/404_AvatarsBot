from botty import CompositeHandler

from . import get_commands, send_picture, start, text

handler = CompositeHandler(
    start.handler,
    get_commands.handler,
    send_picture.handler,
    text.handler,
)

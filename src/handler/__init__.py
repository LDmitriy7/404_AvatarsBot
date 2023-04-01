from botty import CompositeHandler

from . import admin, get_commands, send_picture, start, text

handler = CompositeHandler(
    start.handler,
    get_commands.handler,
    send_picture.handler,
    admin.handler,
    text.handler,
)

from botty import CompositeHandler

from . import command, menu

handler = CompositeHandler(
    command.handler,
    menu.handler,
)

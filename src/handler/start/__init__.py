from botty import CompositeHandler

from . import entry, menu

handler = CompositeHandler(
    entry.handler,
    menu.handler,
)

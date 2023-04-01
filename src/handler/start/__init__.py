from botty import CompositeHandler

from . import menu, start

handler = CompositeHandler(
    start.handler,
    menu.handler,
)

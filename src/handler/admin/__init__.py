from botty import CompositeHandler

from . import admin, broadcast

handler = CompositeHandler(
    admin.handler,
    broadcast.handler,
)

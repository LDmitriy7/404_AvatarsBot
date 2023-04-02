from botty import CompositeHandler

from . import get_another, main_menu, menu

handler = CompositeHandler(
    menu.handler,
    get_another.handler,
    main_menu.handler,
)

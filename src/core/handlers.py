from collections.abc import Mapping
from typing import TypeVar, cast

from botty_core import PTBContext, PTBHandler
from telegram import ext

ObjectT = TypeVar("ObjectT", bound=object)


def listify(obj: ObjectT | None) -> ObjectT | list[ObjectT]:
    """obj -> [obj], list -> list, None -> []."""
    if obj is None:
        return []
    if isinstance(obj, list):
        return obj
    return [obj]


class ConversationHandler(ext.ConversationHandler[PTBContext]):
    def __init__(
        self,
        key: int,
        entry_point: PTBHandler | list[PTBHandler],
        states: Mapping[int, PTBHandler | list[PTBHandler]],
        fallback: PTBHandler | list[PTBHandler] | None = None,
    ) -> None:
        entry_points = cast(list[PTBHandler], listify(entry_point))
        fallbacks = cast(list[PTBHandler], listify(fallback))

        _states = {
            cast(object, state): cast(list[PTBHandler], listify(handler))
            for state, handler in states.items()
        }

        super().__init__(
            entry_points,
            _states,
            fallbacks,
            allow_reentry=True,
            name=str(key),
            persistent=True,
        )

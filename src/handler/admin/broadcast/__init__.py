from core import ConversationHandler
from lib import keys

from . import broadcast, cancel, confirm, post

handler = ConversationHandler(
    key=keys.BROADCAST,
    entry_point=broadcast.handler,
    states={
        keys.POST: post.handler,
        keys.CONFIRM: confirm.handler,
    },
    fallback=cancel.handler,
)

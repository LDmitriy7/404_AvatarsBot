from core import ConversationHandler

from .subhandlers import entry_handler

handler = ConversationHandler("broadcast", entry_handler, states={})

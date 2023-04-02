from botty import MessageContext, MessageHandler

from lib import ConfirmKeyboard, keys, texts


async def callback(ctx: MessageContext) -> int:
    ctx.storage[keys.POST_ID] = ctx.message.id
    await ctx.copy()
    await ctx.reply(texts.BROADCAST_START, ConfirmKeyboard())
    return keys.CONFIRM


handler = MessageHandler(callback)

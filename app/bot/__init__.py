import aiogram.types
from app.core import dp
import app.bot.handlers as handlers
import app.bot.callbacks as callbacks


dp.register_message_handler(handlers.message_handler, content_types=aiogram.types.ContentType.ANY)
dp.register_inline_handler(callbacks.inline_callback_handler)

import re
import hashlib
from app.db import get_last_id
from aiogram.types import InlineQuery, InputTextMessageContent, InlineQueryResultArticle


async def inline_callback_handler(inline_query: InlineQuery):
    value = get_last_id()
    percent = round(value / 10000, 3)
    text = f"<b>До смерти чата осталось {1000000 - value} сообщений ({value}/1000000) ({percent}%)</b>"
    result_id = hashlib.md5(text.encode()).hexdigest()
    answer = InlineQueryResultArticle(
        id=result_id,
        title=re.sub(r"<[^>]*>", "", text),
        input_message_content=InputTextMessageContent(text, parse_mode="html")
    )

    return await inline_query.answer(results=[answer], cache_time=0)

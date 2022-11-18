from app.config import CHAT_ID
from app.db import write_last_id
from aiogram.types import Message


async def message_handler(message: Message):
    message_id = message.message_id
    if message_id > 1000000 or message.chat.id != CHAT_ID:
        await message.answer("Смерть")
        return await message.bot.leave_chat(message.chat.id)

    write_last_id(message_id)
    print(f"successfully written {message_id}")

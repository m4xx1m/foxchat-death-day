import app.bot
from aiogram import executor

if __name__ == '__main__':
    print("Starting")
    executor.start_polling(app.bot.dp, skip_updates=False)

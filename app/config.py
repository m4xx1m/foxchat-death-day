import os

DB_FILE   = "db/last_id"
CHAT_ID   = int(os.getenv("CHAT_ID", -1001441540954))
BOT_TOKEN = os.getenv("BOT_TOKEN", None)
if not BOT_TOKEN:
    print("NO BOT TOKEN")
    exit(-1)

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "wb") as db_file:
        db_file.write(b'0')

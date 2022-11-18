from app.config import DB_FILE

VALUE_CACHE: int | None = None


def get_last_id() -> int:
    if VALUE_CACHE:
        return VALUE_CACHE
    else:
        with open(DB_FILE, "rb") as db_file:
            value = db_file.read().strip()

            if value.isdigit():
                return int(value)
            else:
                raise ValueError("Invalid db file")


def write_last_id(value: int):
    with open(DB_FILE, "wb") as db_file:
        db_file.write(str(value).encode())

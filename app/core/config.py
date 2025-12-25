from pathlib import Path
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent.parent

class Settings(BaseModel):
    database_url: str = f"sqlite:///{BASE_DIR}/db.sqlite3"
    debug: bool = True

settings = Settings()

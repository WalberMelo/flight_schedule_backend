import os
from dotenv import load_dotenv

load_dotenv()  # only needed locally, not on AWS

from typing import Optional

class Settings:
    AVIATIONSTACK_KEY: Optional[str] = os.getenv("AVIATIONSTACK_KEY")
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")

settings = Settings()
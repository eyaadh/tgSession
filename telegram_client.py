from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()
API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')


SESSION_DIR = "sessions"
os.makedirs(SESSION_DIR, exist_ok=True)
# proxy = (socks.SOCKS5, "127.0.0.1", 9050)


def normalize_phone(phone: str) -> str:
    phone = phone.strip().replace(" ", "")  # 🧼 remove all spaces
    return phone if phone.startswith("+") else f"+{phone}"

def get_session_file(phone: str) -> str:
    phone = normalize_phone(phone)
    return os.path.join(SESSION_DIR, f"{phone}.session")

def create_client(phone: str) -> TelegramClient:
    session_path = get_session_file(phone)
    return TelegramClient(session_path, API_ID, API_HASH)
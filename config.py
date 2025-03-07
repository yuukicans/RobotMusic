from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "00"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/0qe835.jpg")
START_IMG = getenv("START_IMG", "https://files.catbox.moe/0qe835.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/YuukiMusicSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tentangyuuki")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "422998061").split()))


FAILED = "https://files.catbox.moe/0qe835.jpg"

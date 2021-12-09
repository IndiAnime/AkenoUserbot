import os

API_HASH = os.getenv("API_HASH")
API_ID = int(os.getenv("API_ID"))
ALIVE_IMG = os.getenv("ALIVE_IMG", "https://telegra.ph/file/4c8b7654e0cff9d9cd0ee.jpg")
MONGO_URI = os.getenv("MONGO_URI")
PYRO_SESSION = os.getenv("PYRO_SESSION")
TELE_SESSION = os.getenv("TELE_SESSION")
PREFIX = os.getenv("PREFIX", "?")
LOG_CHAT = int(os.getenv("LOG_CHAT"))
HEROKU_API = os.getenv("HEROKU_API")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

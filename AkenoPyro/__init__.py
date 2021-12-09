# Copyright (C) 2021 by Achu biju
#
# This file is part of < https://github.com/okay-retard/ZectUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/IndiAnime/AkenoUserBot/blob/main/LICENSE>
#
# All rights reserved.

import logging
import sys
import time
from pyrogram import Client, errors
from config import API_HASH, API_ID, PYRO_SESSION
import logging

import logging

logging.basicConfig(
    filename="app.txt",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
LOGGER = logging.getLogger(__name__)

HELP = {}
CMD_HELP = {}

StartTime = time.time()

API_ID = API_ID
API_HASH = API_HASH
PYRO_SESSION = PYRO_SESSION
plugins = dict(root="AkenoPyro/modules")
app = Client(PYRO_SESSION, api_id=API_ID, api_hash=API_HASH, plugins=plugins)

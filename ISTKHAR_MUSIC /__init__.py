# -----------------------------------------------
# 🔸 ISTKHAR_MUSIC Project
# 🔹 Developed & Maintained by: ISTKHAR Bots (https://github.com/TEAM-ISTKHAR)
# 📅 Copyright © 2025 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by TEAM-ISTKHAR
# -----------------------------------------------


from ISTKHAR_MUSIC.core.bot import ISTKHAR
from ISTKHAR_MUSIC.core.dir import dirr
from ISTKHAR_MUSIC.core.git import git
from ISTKHAR_MUSIC.core.userbot import Userbot
from ISTKHAR_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ISTKHAR()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

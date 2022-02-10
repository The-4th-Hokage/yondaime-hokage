import enum
import gzip
import io
import json
import os
import zipfile
from pathlib import Path
from typing import List

import dotenv

BASE_DIR = Path(
    __file__).resolve().parent.parent.parent  # In minato_namikaze/ folder
dotenv_file = Path(__file__).resolve().parent.parent.parent.parent / ".env"


def token_get(tokenname):
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
    return os.environ.get(tokenname, "False").strip("\n")


api_image_store_dir = BASE_DIR / "images_api_store"

DEFAULT_COMMAND_SELECT_LENGTH = 25


class BotList(enum.Enum):
    dblst = token_get("DISCORDBOTLIST")
    discordbotsgg = token_get("DISCORDBOTSGG")
    topken = token_get("TOPGG")
    bfd = token_get("BOTSFORDISCORD")
    botlist = token_get("BOTLISTSPACE")  # discordlistspace
    discordboats = token_get("DISCORDBOATS")
    voidbot = token_get("VOIDBOT")
    fateslist = token_get("FATESLIST")
    bladebot = token_get("BLADEBOT")
    discordlabs = token_get("DISCORDLABS")
    infinity = token_get("INFINITY")


class ShinobiMatch(list, enum.Enum):
    character_side_exclude = [
        "anbu",
        "iwagakure",
        "kumogakure",
        "kirigakure",
        "otogakure",
        "sunagakure",
        "akatsuki",
        "konohagakure",
    ]

    name_exclusion = character_side_exclude + [
        "naruto",
        "sasuke"
        "jiraya",
        "namikaze",
        "sarutobi",
        "yamanaka",
        "akimichi",
        "aburame",
        "uzumaki",
        "hyuga",
        "otsutsuki",
        "nara",
        "senju",
        "uchiha",
        "kakashi",
        "sakura",
    ]


@enum.unique
class ChannelAndMessageId(enum.IntEnum):
    badges_channel = 920536143458598930
    backup_channel = 922544732918415390
    error_logs_channel = 920190310942908513

    server_id = 920190307595874304
    server_id2 = 920536143244709889

    tags = 920536143458598931
    tags_aliases = 922539699409661972

    restartlog_channel1 = 920190310942908508
    restartlog_channel2 = 920536143458598926

    serverlog_channel1 = 920190310942908509
    serverlog_channel2 = 920536143458598927


class Tokens(enum.Enum):
    statcord = token_get("STATCORD")
    dagpi = token_get("DAGPI")
    chatbot = token_get("CHATBOTTOKEN")
    sentry_link = token_get("SENTRY")

    tenor = token_get("TENOR")
    giphy = token_get("GIPHY")

    token = token_get("TOKEN")
    weather = token_get("WEATHER")


class LinksAndVars(enum.Enum):
    website = token_get("WEBSITE")

    github = "https://github.com/The-4th-Hokage/yondaime-hokage"
    github_branch = "master"

    statuspage_link = "https://minatonamikaze.statuspage.io/"

    version = token_get("VERSION")
    invite_code = "wXVQahNM5c"
    timeout = 3.0
    owner_ids = [887549958931247137, 837223478934896670, 747729781369602049]

    with gzip.open(
            os.path.join(
                Path(__file__).resolve().parent.parent, "data",
                "insult.txt.gz"),
            "rt",
            encoding="utf-8",
    ) as f:
        insults: List[str] = list(
            map(
                lambda a: a.strip(" ").strip("\n").strip("'").strip('"').strip(
                    "\\"),
                f.read().split(","),
            ))


class RaidMode(enum.Enum):
    off = 0
    on = 1
    strict = 2


with open(
        os.path.join(
            Path(__file__).resolve().parent.parent, "data",
            "listing.json")) as f:
    listing: dict = json.load(f)

with gzip.open(
        os.path.join(
            Path(__file__).resolve().parent.parent,
            "data",
            "periodic_table_data",
            "LATTICES.json.gz",
        ),
        "rt",
        encoding="utf-8",
) as f:
    LATTICES: dict = json.load(f)

with gzip.open(
        os.path.join(
            Path(__file__).resolve().parent.parent,
            "data",
            "periodic_table_data",
            "IMAGES.json.gz",
        ),
        "rt",
        encoding="utf-8",
) as f:
    IMAGES: dict = json.load(f)

with gzip.open(
        os.path.join(
            Path(__file__).resolve().parent.parent,
            "data",
            "periodic_table_data",
            "UNITS.json.gz",
        ),
        "rt",
        encoding="utf-8",
) as f:
    UNITS: dict = json.load(f)

database_category_name = "DATABASE"
database_channel_name = "setup vars"
antiraid_channel_name = "antiraid"
mentionspam_channel_name = "mentionspam"
reaction_roles_channel_name = "reaction roles"

minato_gif = []
with zipfile.ZipFile(BASE_DIR /
                     os.path.join("lib", "data", "minato.zip")) as myzip:
    for i in myzip.namelist():
        with myzip.open(i) as f:
            minato_gif.append((i, io.BytesIO(f.read())))

with zipfile.ZipFile(BASE_DIR /
                     os.path.join("lib", "data", "among_us.zip")) as myzip:
    with myzip.open("amongus.png") as f:
        among_us = io.BytesIO(f.read())
    with myzip.open("amoungus_friends.png") as f:
        among_us_friends = (i, io.BytesIO(f.read()))

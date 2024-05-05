import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("25655555"))
API_HASH = os.getenv("57b330d11c2e758e6e3514ffc586bad5")
SESSION = os.getenv("BAGHeQMAj2-ZV5D0nH0uncl66w1aEg6wjaAiEj4i2Pdj_4qdevLf0JH5__qw1xi0Tr1riLs-2HQasaP7-mK5_XoXgqxfjGtBrFj5xyhSXC32UYFsG242IpSNs9MFX_nCgw5zkRg6ZgNCYP-dax3aQT0EvOCf8b8Nvr6TqC4f7tq9-MhLxzQzr7V0xMPlW2kEiKsGilL5zQQXIUnD9QCyWmP8uJ1mSE5K2-SeMuXLF-g9qlFH2o0r0UwACLronmGRCS1bb_JOicdxHCzjrM4nEiM9po3moAoLX_nUoY0RCB3NXtDdsxIX3P0ggrK4Z2O4TdUdBnaBvuxtnu3FPyJ3WchYzdQXBwAAAAF9jK6EAA")
HNDLR = os.getenv("HNDLR", "/")
SUDO_USERS = list(map(int, os.getenv("6401339012").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)

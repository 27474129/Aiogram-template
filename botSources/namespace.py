from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
from .inlinekeyboards import InlineKeyboards
from .defaultkeyboards import DefaultKeyboards
import os
import asyncio
import logging


load_dotenv()

storage = MemoryStorage()
bot = Bot(os.getenv("BOT_TOKEN"), parse_mode="HTML")
dp = Dispatcher(bot, storage=storage, loop=asyncio.get_event_loop())

logger = logging.getLogger()

inline = InlineKeyboards()
default = DefaultKeyboards()
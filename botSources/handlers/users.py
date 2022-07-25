# Users handlers
from aiogram import types
from aiogram import filters as defaultfilters
from aiogram.dispatcher import FSMContext
from ..namespace import *
from ..states import Client
from ..filters import *
from ..sql import Mysql
from datetime import datetime

import os
import logging
import asyncio
import re


@dp.message_handler(defaultfilters.CommandStart())
async def commandStartHandler(message: types.Message):
    await message.answer("Hello, World!")
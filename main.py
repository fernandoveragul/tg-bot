import logging

from aiogram.utils import executor
from bot.example import dp

from asyncio import new_event_loop, set_event_loop
set_event_loop(new_event_loop())

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp)


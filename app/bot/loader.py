import os 
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler


bot = Bot(token=os.getenv('bot_token'), parse_mode='html')
storage = RedisStorage2(host=os.getenv('redis_host', 'localhost'), port=int(os.getenv('redis_port', 6379)), db=int(os.getenv('redis_db')))
dp = Dispatcher(bot=bot, storage=storage)

scheduler = AsyncIOScheduler()

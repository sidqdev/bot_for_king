from aiogram import types

from app.bot.loader import dp
from app.bot import handlers


dp.register_message_handler(handlers.start, commands='start', state=None)
dp.register_chat_join_request_handler(handlers.approve, state='*')

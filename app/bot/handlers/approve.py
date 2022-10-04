from aiogram.types import ChatJoinRequest
from aiogram.dispatcher.storage import FSMContext
from app.database import user, text
from app.bot.loader import bot


async def approve(request: ChatJoinRequest, state: FSMContext):
    await request.approve()
    await user.approve_chat_request(request.from_user.id)
    await bot.send_message(request.from_user.id, await text.get('spam'))
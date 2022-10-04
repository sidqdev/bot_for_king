from aiogram.types import Message
from aiogram.dispatcher.storage import FSMContext
from app.database import user, text


async def start(message: Message, state: FSMContext):
    await user.add(message.from_user.id, message.from_user.full_name)
    await state.set_state('started')
    await message.answer(await text.get('start'))

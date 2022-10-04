from app.bot.loader import scheduler, bot
from app.database import user, text
import asyncio


async def send_notification():
    interval = 0
    message = await text.get('spam')
    users = await user.get_for_spam(interval)
    for usr in users:
        try:
            await bot.send_message(usr.get('id'), text=message.format(name=usr.get('name')))
            await asyncio.sleep(0.04)
        except:
            pass



# scheduler.add_job(send_notification, 'interval', seconds=60)
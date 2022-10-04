from ._core import connection
from asyncpg import Connection


@connection
async def add(id: int, name: str, conn: Connection = None):
    q = '''INSERT INTO bot_user(id, name, created_at)
           VALUES($1, $2, NOW())
           ON CONFLICT(id) DO NOTHING'''
    await conn.execute(q, id, name)


@connection
async def approve_chat_request(id: int, conn: Connection = None):
    q = '''UPDATE bot_user 
           SET enter_at_chat_time = NOW()
           WHERE id = $1'''

    await conn.execute(q, id)

    
@connection
async def get_for_spam(timedelta, conn: Connection = None) -> list:
    q = '''SELECT id, name
           FROM bot_user
           WHERE enter_at_chat_time IS NOT NULL AND NOT spamed AND enter_at_chat_time + interval '$1 minutes' < NOW() '''
    users = [dict(x) for x in await conn.fetch(q, timedelta)]
    ids = [x.get('id') for x in users]

    q = '''UPDATE bot_user
           SET spamed = True
           WHERE id = ANY($1)'''
    await conn.execute(q, ids)

    return users

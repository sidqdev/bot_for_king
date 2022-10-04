from ._core import connection
from asyncpg import Connection


@connection
async def get(id: str, conn: Connection = None):
    q = '''SELECT text
           FROM bot_text
           WHERE id = $1'''
    return await conn.fetchval(q, id)


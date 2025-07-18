import asyncio
import aiosqlite

DB_NAME = "users.db"

async def async_fetch_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            result = await cursor.fetchall()
            print(f'All result: ', result)
            return result
        

async def async_fetch_older_users():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            result = await cursor.fetchall()
            print("User older than 40", result)
            return result
    

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently)

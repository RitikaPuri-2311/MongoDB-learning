from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.day4_db

async def run_transaction():
    async with await client.start_session() as session:
        async with session.start_transaction():
            try:
                await db.users.insert_one(
                    {"name": "Motor User", "role": "Viewer"},
                    session=session
                )

                await db.logs.insert_one(
                    {"action": "User Created", "status": "success"},
                    session=session
                )

                print("Transaction Success")

            except Exception as e:
                print("Transaction Failed:", e)

asyncio.run(run_transaction())
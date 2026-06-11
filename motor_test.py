from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def main():

    client = AsyncIOMotorClient(
        "mongodb://localhost:27017"
    )

    db = client.document_management_db

    user = await db.users.find_one(
        {
            "name": "Ritika"
        }
    )

    print(user)

asyncio.run(main())
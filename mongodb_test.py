from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["document_management_db"]

users = db["users"]
'''
result = users.insert_one({     #insert a single document into the users collection
    "name": "Python User",
    "email": "python@gmail.com",
    "role": "Viewer"
})

print("Inserted ID:", result.inserted_id)
'''
'''
result = users.insert_many([    #insert multiple documents into the users collection
    {
        "name": "Aman",
        "email": "aman@gmail.com",
        "role": "Editor"
    },
    {
        "name": "Priya",
        "email": "priya@gmail.com",
        "role": "Viewer"
    }
])

print(result.inserted_ids)
'''
'''
user = users.find_one(    
    {
        "name": "Ritika"
    }
)

print(user)

for user in users.find():
    print(user)
'''
for user in users.find(
    {
        "role": "Viewer"
    }
):
    print(user)

result = users.update_one(
    {
        "name": "Python User"
    },
    {
        "$set": {
            "role": "Admin"
        }
    }
)

print("Modified:", result.modified_count)

result = users.update_many(
    {
        "role": "Viewer"
    },
    {
        "$set": {
            "is_active": True
        }
    }
)

print("Modified:", result.modified_count)

pipeline = [
    {
        "$group": {
            "_id": "$role",
            "count": {
                "$sum": 1
            }
        }
    }
]

result = users.aggregate(pipeline)

for doc in result:
    print(doc)
from connection import users_collection


def getdata():
    users = list(users_collection.find({}, {"_id": 0}))
    return [user["value"] for user in users]


def add_user(value):
    if not value:
        raise ValueError("value is required")

    users_collection.insert_one({"value": value})
    return {"message": "User added successfully"}


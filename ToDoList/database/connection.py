from pymongo import MongoClient

MONGO_DETAILS = "mongodb://localhost:27017"
client = MongoClient(MONGO_DETAILS)

database = client.todo_database
task_collection = database.get_collection("tasks")
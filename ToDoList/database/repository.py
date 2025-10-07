from bson.objectid import ObjectId
from datetime import datetime
from .connection import task_collection 
from starlette.concurrency import run_in_threadpool


def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "status": task["status"],
        "created_at": task["created_at"],
    }


async def add_task(task_data: dict) -> dict:
    def _add():
        task_data["status"] = "pending"
        task_data["created_at"] = datetime.utcnow()

        new_task = task_collection.insert_one(task_data)
        created_task = task_collection.find_one({"_id": new_task.inserted_id})
        return task_helper(created_task)

    return await run_in_threadpool(_add)


async def retrieve_tasks() -> list:
    def _get_all():
        tasks = []
        for task in task_collection.find():
            tasks.append(task_helper(task))
        return tasks

    return await run_in_threadpool(_get_all)


async def retrieve_task(id: str) -> dict | None:
    def _get_one():
        task = task_collection.find_one({"_id": ObjectId(id)})
        if task:
            return task_helper(task)
        return None

    return await run_in_threadpool(_get_one)


async def update_task(id: str,  data:  dict) -> bool:
    def _update():
        data_to_update = {k: v for k, v in data.items() if v is not None}

        if len(data_to_update) >= 1:
            result = task_collection.update_one(
                {"_id": ObjectId(id)},{"$set": data_to_update}
            )
            return result.modified_count > 0
        return False

    return await run_in_threadpool(_update)


async def delete_task(id:str) -> bool:
    def _delete():
        result = task_collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0

    return await run_in_threadpool(_delete)

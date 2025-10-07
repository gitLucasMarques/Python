from database import repository
from schemas.task import TaskCreate, TaskUpdate
from bson.objectid import ObjectId
from fastapi import HTTPException

async def create_new_task(task_data: TaskCreate):

    task_dict = task_data.model_dump()
    new_task = await repository.add_task(task_dict)
    return new_task

async def get_all_tasks():

    tasks = await repository.retrieve_tasks()
    return tasks

async def get_task_by_id(task_id: str):
    
    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail="Invalid task ID")

    task = await repository.retrieve_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task

async def update_existing_task(task_id: str, task_data: TaskUpdate):

    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail="Invalid task ID")
    
    existing_task = await get_task_by_id(task_id)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_data.model_dump(exclude_unset=True)
    sucess = await repository.update_task(task_id, update_data) 

    if not sucess:
        raise HTTPException(status_code=500, detail="Failed to update task")

    updated_task = await repository.retrieve_task(task_id)
    return updated_task

async def delete_task_buy_id(task_id: str):

    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail="Invalid task ID")
    
    try:
        sucess = await repository.delete_task(task_id)
    except Exception as e:
        # Bubble up unexpected repository errors as 500 so caller can see details
        raise HTTPException(status_code=500, detail=f"Error deleting task: {e}")

    if not sucess:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}




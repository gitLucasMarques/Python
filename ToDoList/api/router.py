from fastapi import APIRouter, Body, HTTPException, status
from typing import List
from services import task_service
from schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter()

@router.post(
    "/", 
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task"
)

async def create_task(task: TaskCreate):

    new_task = await task_service.create_new_task(task)
    return new_task

@router.get(
    "/",
    response_model=List[TaskResponse],
    summary="Retrieve all tasks"
)

async def get_tasks():

    return await task_service.get_all_tasks()

@router.get(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Retrieve a task by ID"
)

async def get_task(task_id: str):
    
    task = await task_service.get_task_by_id(task_id)
    return task

@router.put(
    "/{task_id}",
    response_model=TaskResponse,
    summary="Update a task by ID"
)

async def update_task(task_id: str, task: TaskUpdate):

    result = await task_service.update_existing_task(task_id, task)
    return result

@router.delete(
    "/{task_id}",
    response_model=dict,
    summary="Delete a task by ID"
)

async def delete_task(task_id: str):

    result = await task_service.delete_task_buy_id(task_id)
    return result


from sqlmodel import select, Session
from utils import schemas
from database.models import Tasks
from fastapi import status


def create(data: schemas.CreateTask, db: Session):
    try:
        new_task = Tasks(user_id=data.user_id,
                         task=data.task, status=data.status)
        db.add(new_task)
        db.commit()
        return {
            "msg": f"Task {new_task.task_id} created successfully"
        }
    except Exception as e:
        print(f"Error in creating task - {e}")
        return {
            "msg": f"Error in creating task - {e}"
        }


def read(user_id: int, db: Session):
    try:
        with db:
            query = select(Tasks).where(Tasks.user_id == user_id)
            result = db.exec(query).all()
            return result
    except Exception as e:
        print(f"Error in read task - {e}")
        return {
            "msg": f"Error in reading task - {e}"
        }


def delete(task_id: int, db: Session):
    try:
        with db:
            query = select(Tasks).where(Tasks.task_id == task_id)
            task = db.exec(query).one()
            db.delete(task)
            db.commit()
            print(f"{task_id} successfully deleted")
            return {
                "msg": f"Task {task_id} successfully deleted"
            }
    except Exception as e:
        print(f"Error in delete task - {e}")
        return {
            "msg": f"Error in delete task - {e}"
        }


def update(data: schemas.UpdateTask, db: Session):

    try:
        query = select(Tasks).where(Tasks.user_id ==
                                    data.user_id, Tasks.task_id == data.task_id)
        current_obj = db.exec(query).first()
        current_obj.task = data.task
        current_obj.status = data.status
        db.commit()
        return {
            "msg": f"Task {data.task_id} updated successfully"
        }
    except Exception as e:
        print(f"Error in update task - {e}")

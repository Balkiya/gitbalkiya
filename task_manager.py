from typing import List
from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def update_task_status(self, task_id: int, new_status: str) -> None:
        updated_tasks = []
        for task in self.tasks:
            if task.task_id == task_id:
                updated_task = task.update_status(new_status)
                updated_tasks.append(updated_task)
            else:
                updated_tasks.append(task)
        self.tasks = updated_tasks

    def filter_tasks(self, condition) -> List[Task]:
        return [task for task in self.tasks if condition(task)]

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

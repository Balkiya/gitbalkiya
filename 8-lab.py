from task import Task
from task_manager import TaskManager

def main():
    task_manager = TaskManager()

    task1 = Task(task_id=1, description="Task 1", state="New")
    task2 = Task(task_id=2, description="Task 2", state="New")
    task3 = Task(task_id=3, description="Task 3", state="In Progress")

    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)

    task_manager.update_task_status(task_id=1, new_status="Completed")

    print("All tasks:")
    for task in task_manager.get_all_tasks():
        print(task)

    print("\nTasks in Progress:")
    in_progress_tasks = task_manager.filter_tasks(lambda task: task.state == "Completed")
    for task in in_progress_tasks:
        print(task)

if __name__ == "__main__":
    main()

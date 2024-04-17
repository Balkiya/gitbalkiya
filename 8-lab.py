from typing import List
from enum import Enum
from dataclasses import dataclass

# Определение перечисления для состояния задачи
class TaskState(Enum):
    Pending = 1
    InProgress = 2
    Completed = 3

# Определение класса для задачи
@dataclass(frozen=True)  # Декоратор для создания неизменяемого класса
class Task:
    task_id: int
    description: str
    state: TaskState = TaskState.Pending

# Функция для создания новой задачи
def create_task(task_id: int, description: str) -> Task:
    return Task(task_id, description)

# Функция для обновления состояния задачи
def update_task_state(task: Task, new_state: TaskState) -> Task:
    return Task(task.task_id, task.description, new_state)

# Функция для получения списка задач в определенном состоянии
def tasks_in_state(tasks: List[Task], state: TaskState) -> List[Task]:
    return list(filter(lambda task: task.state == state, tasks))

# Пример использования
if __name__ == "__main__":
    # Создание нескольких задач
    task1 = create_task(1, "Подготовить отчет")
    task2 = create_task(2, "Провести встречу")
    task3 = create_task(3, "Завершить проект")

    # Обновление состояния задачи
    task2 = update_task_state(task2, TaskState.InProgress)

    # Получение списка задач в определенном состоянии
    tasks_pending = tasks_in_state([task1, task2, task3], TaskState.Pending)
    tasks_in_progress = tasks_in_state([task1, task2, task3], TaskState.InProgress)
    tasks_completed = tasks_in_state([task1, task2, task3], TaskState.Completed)

    # Вывод результатов
    print("Задачи в ожидании:")
    for task in tasks_pending:
        print(task)

    print("\nЗадачи в процессе выполнения:")
    for task in tasks_in_progress:
        print(task)

    print("\nЗавершенные задачи:")
    for task in tasks_completed:
        print(task)

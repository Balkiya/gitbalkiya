class Task:
    def __init__(self, task_id, description, state):
        self.task_id = task_id
        self.description = description
        self.state = state

    def __repr__(self):
        return f"Task(task_id={self.task_id}, description='{self.description}', state='{self.state}')"

    def update_status(self, new_status):
        return Task(self.task_id, self.description, new_status)

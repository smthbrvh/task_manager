from models.task import Task
from services.file_handler import FileHandler

class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        if not task in self.__tasks:
            self.__tasks.append(task)
        else:
            print("That task is already exists")

    def delete_task(self, id):
        self.__tasks = [t for t in self.__tasks if t.get_id() != id]

    def list(self):
        return self.__tasks

    def get_task(self, id):
        for task in self.list():
            if task.get_id() == id:
                return task
        return None

    def update_status(self, id, status):
        task = self.get_task(id)
        if task is None:
            return False
        else:
            return task.change_status(status)

    def get_filtered_tasks(self, status):
        statuses = ["all", "todo", "in-progress", "done"]
        status = status.lower()
        if status not in statuses:
            return None
        elif status == "all":
            return self.list()
        else:
            return [task for task in self.list() if task.return_status() == status]

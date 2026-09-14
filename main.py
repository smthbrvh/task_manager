from datetime import datetime
import json

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

class Task():
    taskId = 1
    def __init__(self, desc):
        self.__id = Task.taskId
        self.__description = desc
        self.__status = "todo"
        self.__created = datetime.now()
        self.__updated = datetime.now()
        Task.taskId += 1

    def return_task(self, id, description, status, created_at, updated_at):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__created = created_at
        self.__updated = updated_at

    def return_status(self):
        return self.__status

    def print_task(self):
        print(f"{self.__id:<4} {self.__description:<30} {self.__status:<10}")

    def change_des(self, description):
        self.__description = description

    def get_id(self):
        return self.__id

    def change_status(self, status):
        statuses = ["todo", "done", "in-progress"]
        if status.lower() not in statuses:
            return False
        else:
            self.__status = status.lower()
            return True

    def to_dict(self):
        return {
            "id": self.__id,
            "description": self.__description,
            "status": self.__status,
            "created_at": self.__created.strftime("%Y-%m-%d %H:%M"),
            "updated_at": self.__updated.strftime("%Y-%m-%d %H:%M"),
        }



class TaskManagerApllication():
    def __init__(self):
        self.__taskmanager = TaskManager()
        self.__filehandler = FileHandler("task.json")


        data = self.__filehandler.load_file()

        if data is None:
            return
        else:
            for task in data:
                new_task = Task(task["description"])
                new_task.return_task(task["id"], task["description"], task["status"], datetime.strptime(task["created_at"], "%Y-%m-%d %H:%M"), datetime.strptime(task["updated_at"], "%Y-%m-%d %H:%M"))
                self.__taskmanager.add_task(new_task)
            

    def exit(self):
        self.__filehandler.save_file(self.__taskmanager.list())

    def help(self):
        print("commands: ")
        print("exit")
        print("add")
        print("list (all)")
        print("lstat")
        print("update")
        print("updstat")
        print("delete")

    def add(self):
        desc = input("Description: ")
        self.__taskmanager.add_task(Task(desc))

    def list(self):
        status = input("Status: (all, to-do, in-progress, done)")
        print("All tasks: ")
        print(f"{"ID":<4} {"Description":<30} {"Status":<10}")
        result = self.__taskmanager.get_filtered_tasks(status)
        if result is None:
            print("Couldnt return tasks.")
        else:
            for task in result:
                task.print_task()

    def update(self):
        id = int(input("ID: "))

        task = self.__taskmanager.get_task(id)
        if task is None:
            print("Task not found")
        else:
            new_description = input("New description: ")
            task.change_des(new_description)

    def delete(self):
        id = int(input("ID: "))
        self.__taskmanager.delete_task(id)
        print("Task has been deleted.")

    def update_status(self):
        id = int(input("ID: "))
        status = input("Status: (todo, in-progress, done)")
        request = self.__taskmanager.update_status(id, status)
        if request:
            print("Status updated successfully")
        else:
            print("Couldnt update status.")
                            
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("Command: ").lower()
            if command == "exit":
                self.exit()
                break
            elif command == "add":
                self.add()
            elif command == "list":
                self.list()
            elif command == "update (description)":
                self.update()
            elif command == "delete":
                self.delete()
            elif command == "updstat":
                self.update_status()



class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        try:
            with open(self.__filename) as f:
                data = json.load(f)
                return data
        except (json.JSONDecodeError, FileNotFoundError):
            return None

    def save_file(self, tasks: list):
        with open(self.__filename, "w") as f:
            json.dump([p.to_dict() for p in tasks], f, indent=4)

application = TaskManagerApllication()
application.execute()
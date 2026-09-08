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

    def list(self):
        return self.__tasks

    def get_task(self, id):
        for task in self.list():
            if task.get_id() == id:
                return task
        return None
                

class Task():
    taskId = 1
    def __init__(self, desc):
        self.__id = Task.taskId
        self.__description = desc
        self.__status = "To do"
        self.__created = datetime.now()
        self.__updated = datetime.now()
        Task.taskId += 1

    def return_task(self, id, description, status, created_at, updated_at):
        self.__id = id
        self.__description = description
        self.__status = status
        self.__created = created_at
        self.__updated = updated_at

    def print_task(self):
        print(f"{self.__id:<4} {self.__description:<30} {self.__status:<10}")

    def change_des(self, description):
        self.__description = description

    def get_id(self):
        return self.__id

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
        print("list")
        print("update")
        print("delete")

    def add(self):
        desc = input("Description: ")
        self.__taskmanager.add_task(Task(desc))

    def list(self):
        print("All tasks: ")
        print(f"{"ID":<4} {"Description":<30} {"Status":<10}")
        result = self.__taskmanager.list()
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
        pass
    ###TO DO
                            
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
            elif command == "update":
                self.update()
            elif command == "delete":
                self.delete()



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
from datetime import date
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

    def update(self, id):
        for task in self.__tasks:
            if task.__id == id:
                pass
                

class Task():
    taskId = 1
    def __init__(self, desc):
        self.__id = Task.taskId
        self.__description = desc
        self.__status = "TO do"
        self.__created = date.today()
        self.__updated = date.today()
        Task.taskId += 1

    def desc(self):
        print(self.__description)

    def change_des(self, description):
        self.__description = description

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

        #Add loading files from a file here

    def exit(self):
        self.__filehandler.save_file(self.__taskmanager.list())

    def help(self):
        print("commands: ")
        print("exit")
        print("add")
        print("list")

    def add(self):
        desc = input("Description: ")
        self.__taskmanager.add_task(Task(desc))

    def list(self):
        print("All tasks: ")
        result = self.__taskmanager.list()
        for task in result:
            print(task.desc())

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


class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        pass

    def save_file(self, tasks: list):
        with open(self.__filename, "w") as f:
            for task in tasks:
                json.dump(task.to_dict(), f, indent=4)

application = TaskManagerApllication()
application.execute()
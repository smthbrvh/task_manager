from datetime import date

class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        if not task in self.__tasks:
            self.__tasks.append(task)
        else:
            print("That task is already exists")

    def list(self):
        for task in self.__tasks:
            task.desc()

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



class TaskManagerApllication():
    def __init__(self):
        self.__taskmanager = TaskManager()

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
        self.__taskmanager.list()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("Command: ").lower()
            if command == "exit":
                break
            elif command == "add":
                self.add()
            elif command == "list":
                self.list()

application = TaskManagerApllication()
application.execute()
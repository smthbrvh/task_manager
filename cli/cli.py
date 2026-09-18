from services.file_handler import FileHandler
from services.task_manager import TaskManager
from datetime import datetime
from models.task import Task


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
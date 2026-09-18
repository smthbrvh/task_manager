import json

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
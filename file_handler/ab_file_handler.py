import abc
import json


class FileHandler(abc.ABC):

    def __init__(self, filename: str, ext: str, ) -> None:
        self.filename = filename
        self.ext = ext

    @abc.abstractmethod
    def read_file(self, filename: str):
        with open(filename, mode='r', encoding='UTF-8') as file:
            return file

    @abc.abstractmethod
    def change_file(self, filename: str, data):
        pass


class JsonFileHandler(FileHandler):

    def __init__(self, filename: str, ext: str = 'json') -> None:
        super().__init__(filename, ext)

    def read_file(self, filename: str) -> list:
        with super().read_file(filename) as file:
            return json.load(file)

    def change_file(self, filename: str, data):
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

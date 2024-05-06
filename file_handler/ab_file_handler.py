import abc
import json


class FileHandler(abc.ABC):

    def __init__(self, ext: str) -> None:
        self.ext = ext

    @abc.abstractmethod
    def read_file(self):
        ...

    @abc.abstractmethod
    def change_file(self):
        ...


class JsonFileHandler(FileHandler):

    def __init__(self, ext: str = 'json') -> None:
        super().__init__(ext)

    def read_file(self) -> list:
        ...

    def change_file(self):
        ...

import json


class JsonFileHandler:
    
    @staticmethod
    def read_file(filename: str) -> list:
        with open(filename, mode='r', encoding='UTF-8') as file:
            return json.load(file)

    @staticmethod
    def write_file(filename: str, data):
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
